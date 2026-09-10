from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel

from instant_python import __version__
from instant_python.cli.instant_python_typer import InstantPythonTyper
from instant_python.config.delivery import cli as config
from instant_python.initialize.delivery import cli as init
from instant_python.metrics.delivery.metrics_middleware import MetricsMiddleware
from instant_python.shared.application_error import ApplicationError
from instant_python.version.delivery.cli import version

app = InstantPythonTyper(cls=MetricsMiddleware)
console = Console()


def version_callback(value: bool) -> None:
    if value:
        console.print(f"instant-python {__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[
        bool | None,
        typer.Option(
            "--version",
            "-V",
            help="Show the application version",
            callback=version_callback,
            is_eager=True,
        ),
    ] = None,
) -> None:
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())

app.add_typer(version.app)

app.add_typer(init.app)
app.add_typer(config.app)


@app.error_handler(ApplicationError)
def handle_application_error(exc: ApplicationError) -> None:
    error_panel = Panel(exc.message, title="Error", border_style="red")
    console.print(error_panel)


@app.error_handler(Exception)
def handle_unexpected_error(exc: Exception) -> None:
    error_panel = Panel(f"An unexpected error occurred: {exc}", title="Error", border_style="red")
    console.print(error_panel)


if __name__ == "__main__":
    app()
