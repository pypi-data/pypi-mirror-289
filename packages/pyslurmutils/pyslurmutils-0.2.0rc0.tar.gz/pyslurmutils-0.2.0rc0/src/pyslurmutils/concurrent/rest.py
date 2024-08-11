import logging
import weakref
from pprint import pformat
from concurrent import futures
from contextlib import ExitStack
from contextlib import contextmanager
from typing import Optional, Generator, Callable, Any

from ..client import SlurmPyConnRestClient
from ..client.job_io.local import RemoteExecutor
from ..client.job_io.local import RemoteWorkerProxy
from ..client.job_io.local import FileConnection
from ..client.job_io.local import TcpConnection
from ..client import defaults

logger = logging.getLogger(__name__)


class SlurmRestFuture(futures.Future):
    def __init__(self) -> None:
        self._job_id = None
        self._slurm_client = None
        super().__init__()

    def job_submitted(self, job_id: int, slurm_client: SlurmPyConnRestClient) -> None:
        """The SLURM job was submitted. It may be running other tasks as well."""
        self._job_id = job_id
        self._slurm_client = weakref.proxy(slurm_client)

    @property
    def job_id(self) -> Optional[int]:
        return self._job_id

    @property
    def slurm_client(self) -> Optional[SlurmPyConnRestClient]:
        return self._slurm_client


class SlurmRestExecutor(RemoteExecutor):
    _FUTURE_CLASS = SlurmRestFuture

    def __init__(
        self,
        url: str = "",
        user_name: str = "",
        token: str = "",
        parameters: Optional[dict] = None,
        log_directory: Optional[str] = None,
        std_split: Optional[bool] = False,
        request_options: Optional[dict] = None,
        pre_script: Optional[str] = None,
        post_script: Optional[str] = None,
        python_cmd: Optional[str] = None,
        initializer: Optional[callable] = None,
        initargs: Optional[tuple] = None,
        initkwargs: Optional[tuple] = None,
        data_directory: Optional[str] = None,
        max_workers: Optional[int] = None,
        max_tasks_per_worker: Optional[int] = 1,
        lazy_scheduling: bool = True,
        conservative_scheduling: bool = False,
    ):
        """
        :param url: SLURM REST API
        :param user_name: User name on SLURM
        :param token: SLURM access token for the user
        :param parameters: SLURM job parameters
        :param log_directory: SLURM log directory
        :param std_split: Split standard output and standard error
        :param request_options: GET, POST and DELETE options
        :param pre_script: Shell script to execute at the start of a job
        :param post_script: Shell script to execute at the end of a job
        :param python_cmd: Python command
        :param initializer: execute when starting a job
        :param initargs: parameters for `initializer`
        :param initkwargs: parameters for `initializer`
        :param data_directory: communicate with the Slum job through files when specified
        :param max_workers: maximum number of Slum jobs that can run at any given time. `None` means unlimited.
        :param max_tasks_per_worker: maximum number of tasks each Slum job can receive before exiting. `None` means unlimited.
        :param lazy_scheduling: schedule SLURM jobs only when needed. Can only be disabled when `max_workers` is specified.
        :param conservative_scheduling: schedule the least amount of workers at the expense of tasks staying longer in the queue.
        """

        self._proxy_kwargs = {
            "max_tasks": max_tasks_per_worker,
            "initializer": initializer,
            "initargs": initargs,
            "initkwargs": initkwargs,
        }

        if data_directory:
            self._file_connection_kwargs = {
                "directory": data_directory,
                "basename": defaults.JOB_NAME,
            }
        else:
            self._file_connection_kwargs = None

        self._slurm_client = SlurmPyConnRestClient(
            url=url,
            user_name=user_name,
            token=token,
            log_directory=log_directory,
            parameters=parameters,
            std_split=std_split,
            request_options=request_options,
            pre_script=pre_script,
            post_script=post_script,
            python_cmd=python_cmd,
        )

        super().__init__(
            max_workers=max_workers,
            max_tasks_per_worker=max_tasks_per_worker,
            lazy_scheduling=lazy_scheduling,
            conservative_scheduling=conservative_scheduling,
        )

    @contextmanager
    def execute_context(
        self,
    ) -> Generator[Callable[[callable, tuple, dict, SlurmRestFuture], Any], None, None]:
        if self._file_connection_kwargs:
            conn_ctx = FileConnection(**self._file_connection_kwargs)
        else:
            conn_ctx = TcpConnection()

        with ExitStack() as stack:
            connection = stack.enter_context(conn_ctx)
            proxy_ctx = RemoteWorkerProxy(connection, **self._proxy_kwargs)
            worker_proxy = stack.enter_context(proxy_ctx)

            job_id = None
            first_submit_kw = None

            def execute(
                task: Callable, args: tuple, kwargs: dict, future: SlurmRestFuture
            ):
                nonlocal job_id, first_submit_kw

                submit_kw = kwargs.pop(defaults.SLURM_ARGUMENTS_NAME, dict())
                if submit_kw is None:
                    submit_kw = dict()

                if job_id is None:
                    first_submit_kw = submit_kw
                    job_id = self._slurm_client.submit_script(worker_proxy, **submit_kw)
                    log_ctx = self._slurm_client.redirect_stdout_stderr(
                        job_id, raise_on_error=False
                    )
                    _ = stack.enter_context(log_ctx)
                elif submit_kw != first_submit_kw:
                    logger.warning(
                        "SLURM submit arguments\n %s\n are ignored in favor of the client arguments\n %s",
                        pformat(submit_kw),
                        pformat(first_submit_kw),
                    )

                future.job_submitted(job_id, self._slurm_client)

                return worker_proxy.execute(task, args=args, kwargs=kwargs)

            yield execute
