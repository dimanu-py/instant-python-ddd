import subprocess
from dataclasses import dataclass

from instant_python.shared.application_error import ApplicationError


@dataclass(frozen=True)
class CommandExecutionResult:
    exit_code: int
    stdout: str
    stderr: str

    def success(self) -> bool:
        return self.exit_code == 0


class SystemConsole:
    def __init__(self, working_directory: str) -> None:
        self._working_directory = working_directory

    def execute(self, command: str) -> CommandExecutionResult:
        try:
            return self._run_command(command)
        except Exception as error:  # noqa: BLE001
            return self._unexpected_error_result(error)

    def execute_or_raise(self, command: str) -> CommandExecutionResult:
        result = self.execute(command)
        if not result.success():
            raise CommandExecutionError(
                exit_code=result.exit_code,
                stderr_output=result.stderr,
            )
        return result

    def _run_command(self, command: str) -> CommandExecutionResult:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            cwd=self._working_directory,
            capture_output=True,
            text=True,
        )
        return CommandExecutionResult(
            exit_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
        )

    @staticmethod
    def _unexpected_error_result(error: Exception) -> CommandExecutionResult:
        return CommandExecutionResult(
            exit_code=-1,
            stdout="",
            stderr=str(error),
        )


class CommandExecutionError(ApplicationError):
    def __init__(self, exit_code: int, stderr_output: str | None = None) -> None:
        message = f"Unexpected error when executing a command, exit code {exit_code}"
        if stderr_output:
            message += f": {stderr_output}"
        super().__init__(message=message)
