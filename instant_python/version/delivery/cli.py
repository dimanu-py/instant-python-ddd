import typer
from rich.console import Console

from instant_python import __version__
from instant_python.version.application.latest_version_printer import LatestVersionPrinter

app = typer.Typer()
console = Console()


@app.command("version", help="Show instant-python version")
def show_version() -> None:
    current_version = __version__
    latest_version = LatestVersionPrinter().execute()
    console.print(f"(current) {current_version} - (latest) {latest_version}")
