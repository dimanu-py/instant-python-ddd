import shutil
import sys
import tempfile

import pytest
from expects import be_false, be_true, contain, equal, expect, raise_error

from instant_python.initialize.infra.env_manager.system_console import CommandExecutionError, SystemConsole


@pytest.mark.integration
class TestSystemCommandExecutor:
    def setup_method(self) -> None:
        self._temp_dir = tempfile.mkdtemp()
        self._console = SystemConsole(working_directory=self._temp_dir)

    def teardown_method(self) -> None:
        shutil.rmtree(self._temp_dir)

    def test_should_execute_command_successfully(self) -> None:
        result = self._console.execute(self._python_command("print('hello')"))

        expect(result.success()).to(be_true)

    def test_should_capture_failing_command(self) -> None:
        result = self._console.execute(self._failing_python_command())

        expect(result.success()).to(be_false)

    def test_should_capture_output_error(self) -> None:
        result = self._console.execute(self._failing_python_command())

        expect(result.stderr).to(contain("captured error"))

    def test_should_capture_empty_stdout_when_no_output(self) -> None:
        result = self._console.execute(self._python_command("pass"))

        expect(result.success()).to(be_true)
        expect(result.stdout).to(equal(""))

    def test_should_return_result_when_execute_or_raise_succeeds(self) -> None:
        result = self._console.execute_or_raise(self._python_command("print('hello')"))

        expect(result.success()).to(be_true)

    def test_should_raise_error_when_execute_or_raise_fails(self) -> None:
        expect(lambda: self._console.execute_or_raise(self._failing_python_command())).to(
            raise_error(CommandExecutionError)
        )

    @staticmethod
    def _python_command(code: str) -> str:
        return f'"{sys.executable}" -c "{code}"'

    @classmethod
    def _failing_python_command(cls) -> str:
        return cls._python_command("import sys; sys.stderr.write('captured error\n'); sys.exit(1)")
