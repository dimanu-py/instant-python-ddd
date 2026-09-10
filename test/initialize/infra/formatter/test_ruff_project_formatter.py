import pytest
from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, raise_error

from instant_python.initialize.infra.env_manager.system_console import CommandExecutionError, SystemConsole
from instant_python.initialize.infra.formatter.ruff_project_formatter import RuffProjectFormatter
from test.initialize.infra.env_manager.mother.command_execution_result_mother import CommandExecutionResultMother


@pytest.mark.unit
class TestRuffProjectFormatter:
    _SUCCESSFUL_COMMAND_RESULT = CommandExecutionResultMother.success()
    _FAILED_COMMAND_RESULT = CommandExecutionResultMother.failure()

    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._ruff_formatter = RuffProjectFormatter(console=self._console)

    def test_should_execute_ruff_formatter(self) -> None:
        expect_call(self._console).execute_or_raise("uvx ruff format").returns(self._SUCCESSFUL_COMMAND_RESULT)

        self._ruff_formatter.format()

        expect(self._console).to(have_been_satisfied)

    def test_should_raise_error_if_format_command_fails(self) -> None:
        expect_call(self._console).execute_or_raise("uvx ruff format").raises(
            CommandExecutionError(
                exit_code=self._FAILED_COMMAND_RESULT.exit_code, stderr_output=self._FAILED_COMMAND_RESULT.stderr
            )
        )

        expect(lambda: self._ruff_formatter.format()).to(raise_error(CommandExecutionError))
