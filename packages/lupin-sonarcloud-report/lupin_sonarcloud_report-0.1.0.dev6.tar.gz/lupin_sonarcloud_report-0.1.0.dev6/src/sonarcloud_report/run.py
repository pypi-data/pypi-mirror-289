import os

import typer

from sonarcloud_report.generate_sonarcloud_project_report import (
    generate_sonarcloud_project_report_file,
)
from sonarcloud_report.__init__ import __version__


cli = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@cli.callback()
def main(
    version: bool = typer.Option(
        None, "--version", callback=version_callback, is_eager=True
    )
):
    pass


@cli.command()
def generate_report():
    typer.echo("SonarCloud report generation started")
    generate_sonarcloud_project_report_file(
        project_name=os.environ.get("CI_PROJECT_NAME"),
        commit_id="2cb96b25c2f2adedae964075c1743073df0a35c6",
        sonar_token=os.environ.get("SONAR_TOKEN"),
    )
    typer.echo("SonarCloud report generation finished")
