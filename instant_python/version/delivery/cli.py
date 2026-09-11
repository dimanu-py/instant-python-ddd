import typer
from rich.console import Console

from instant_python import __version__
from instant_python.version.application.latest_version_printer import LatestVersionPrinter
from instant_python.version.infra.py_pi_version_repository import PyPiVersionRepository
from instant_python.version.infra.urllib_http_client import UrllibHttpClient

app = typer.Typer()
console = Console()


@app.command("version", help="Show instant-python version")
def show_version() -> None:
    current_version = __version__
    latest_version_printer = LatestVersionPrinter(version_repository=PyPiVersionRepository(client=UrllibHttpClient()))
    latest_version = latest_version_printer.execute()
    console.print(f"{current_version} - (latest) {latest_version}")
