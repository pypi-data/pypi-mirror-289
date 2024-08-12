import ipih

from pih import A, PIHThread
from BackupService.const import ROBOCOPY as RBK, PATH
from pih.tools import e, j, lw, nns, nnd, while_not_do
from pih.collections import RobocopyJobDescription, RobocopyJobItem, RobocopyJobStatus

from typing import Callable
from subprocess import CompletedProcess


class BackupApi:
    def start_robocopy_job(
        self, value: RobocopyJobItem, force: bool = False, block: bool = False
    ) -> bool:

        def execute_robocopy_job(value: RobocopyJobItem) -> None:
            job_name: Callable[[], str] = lambda: self.get_job_name(
                name, source, destination
            )
            source: str = nns(value.source)
            destination: str = nns(value.destination)
            name: str = nns(value.name)
            job_path: str = self.get_job_path(name, source, destination)
            job_status: RobocopyJobStatus | None = None
            if not value.live:
                job_status = self.get_job_status(name, source, destination)
                job_status.active = True
                job_status.last_started = A.D.now_to_string(A.CT.ISO_DATETIME_FORMAT)
                self.save_job_status(job_status)
                A.E.backup_robocopy_job_was_started(job_name(), job_status)
            process: CompletedProcess = A.EXC.execute(
                A.EXC.create_command_for_psexec(
                    (RBK.NAME, j((RBK.JOB_PARAMETER_VALUE, job_path))),
                    value.host,
                    interactive=not value.live,
                    run_from_system_account=value.run_from_system_account,
                    run_with_elevetion=value.run_with_elevetion,
                ),
                show_output=True,
                capture_output=False,
            )
            last_status: int = -1
            if value.live:
                pid: int = process.returncode
                job_status = self.get_job_status(name, source, destination)
                job_status.live = True
                job_status.active = True
                job_status.pid = pid
                self.save_job_status(job_status)
                A.E.backup_robocopy_job_was_started(job_name(), job_status)
                while_not_do(
                    lambda: not A.EXC.check_process_is_running(pid, value.host),
                    sleep_time=5,
                )
            else:
                last_status = process.returncode
            job_status = self.get_job_status(name, source, destination)
            job_status.active = False
            job_status.pid = -1
            job_status.last_created = A.D.now_to_string(A.CT.ISO_DATETIME_FORMAT)
            job_status.last_status = last_status
            self.save_job_status(job_status)
            A.E.backup_robocopy_job_was_completed(job_name(), job_status)

        #
        job_status: RobocopyJobStatus = self.get_job_status(
            nns(value.name), nns(value.source), nns(value.destination)
        )
        if not job_status.active or force:
            job_status.active = True
            self.save_job_status(job_status)
            if block:
                execute_robocopy_job(value)
            else:
                PIHThread(execute_robocopy_job, args=(value,))
            
            return True
        return False

    @staticmethod
    def get_job_list() -> list[RobocopyJobItem]:
        rjm: dict[str, dict[str, list[RobocopyJobDescription]]] = nnd(RBK.JOB_MAP)
        result: list[RobocopyJobItem] = []
        for source in rjm:
            for destination in rjm[source]:
                for job_description in rjm[source][destination]:
                    job_item: RobocopyJobItem = A.D.fill_data_from_source(
                        RobocopyJobItem(), job_description
                    )
                    job_item.source = source
                    job_item.destination = destination
                    job_item.name = lw(job_item.name)
                    result.append(job_item)
        return result

    @staticmethod
    def get_job_name(name: str, source: str, destination: str) -> str:
        result: str = ""
        if not e(name):
            result = j((result, name))
            if not e(source):
                result = j((result, A.CT.SPLITTER, source))
                if not e(destination):
                    result = j((result, A.CT_V.ARROW, destination))
        return result

    @staticmethod
    def get_job_status(name: str, source: str, destination: str) -> RobocopyJobStatus:
        return A.R_DS.value(
            A.D_F_B.job_status_name(name, source, destination), RobocopyJobStatus
        ).data or RobocopyJobStatus(name, source, destination)

    @staticmethod
    def save_job_status(value: RobocopyJobStatus) -> bool:
        return A.A_DS.value(
            value,
            A.D_F_B.job_status_name(
                nns(value.name), nns(value.source), nns(value.destination)
            ),
        )

    @staticmethod
    def get_job_path(name: str, source: str, destination: str) -> str:
        return A.PTH.for_windows(
            A.PTH.join(
                PATH.JOB_CONFIG.DIRECTORY_PATH, j((source, destination), "-"), name
            )
        )
