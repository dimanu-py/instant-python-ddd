import pytest
from expects import contain, expect
from typer.testing import CliRunner

from instant_python import __version__
from instant_python.version.delivery.cli import app


@pytest.mark.acceptance
class TestVersionCli:
    def setup_method(self) -> None:
        self._runner = CliRunner()
        
    def test_should_show_installed_version(self) -> None:
        result = self._runner.invoke(app)
        
        expect(result).to(contain(__version__))