import os

import typer

from sonarcloud_report.generate_sonarcloud_project_report import (
    generate_sonarcloud_project_report_file,
)


cli = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo("0.1.0.dev3")
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
        # commit_id=os.environ.get("CI_COMMIT_SHA"),
        sonar_token=os.environ.get("SONAR_TOKEN"),
    )
    typer.echo("SonarCloud report generation finished")
