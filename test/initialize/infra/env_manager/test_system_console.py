import shutil
import tempfile

from expects import be_false, be_true, contain, equal, expect, raise_error

from instant_python.initialize.infra.env_manager.system_console import CommandExecutionError, SystemConsole


class TestSystemCommandExecutor:
    def setup_method(self) -> None:
        self._temp_dir = tempfile.mkdtemp()
        self._console = SystemConsole(working_directory=self._temp_dir)

    def teardown_method(self) -> None:
        shutil.rmtree(self._temp_dir)

    def test_should_execute_command_successfully(self) -> None:
        result = self._console.execute("echo 'hello'")

        expect(result.success()).to(be_true)

    def test_should_capture_failing_command(self) -> None:
        result = self._console.execute("ls /nonexistent_directory_xyz")

        expect(result.success()).to(be_false)

    def test_should_capture_output_error(self) -> None:
        result = self._console.execute("ls /nonexistent_directory_xyz")

        expect(result.stderr).to(contain("cannot access '/nonexistent_directory_xyz'"))

    def test_should_return_non_zero_exit_code_on_error(self) -> None:
        result = self._console.execute("ls /nonexistent_directory_xyz")

        expect(result.exit_code).to_not(equal(0))

    def test_should_capture_empty_stdout_when_no_output(self) -> None:
        result = self._console.execute("true")

        expect(result.success()).to(be_true)
        expect(result.stdout).to(equal(""))

    def test_should_return_result_when_execute_or_raise_succeeds(self) -> None:
        result = self._console.execute_or_raise("echo 'hello'")

        expect(result.success()).to(be_true)

    def test_should_raise_error_when_execute_or_raise_fails(self) -> None:
        expect(lambda: self._console.execute_or_raise("ls /nonexistent_directory_xyz")).to(
            raise_error(CommandExecutionError)
        )
