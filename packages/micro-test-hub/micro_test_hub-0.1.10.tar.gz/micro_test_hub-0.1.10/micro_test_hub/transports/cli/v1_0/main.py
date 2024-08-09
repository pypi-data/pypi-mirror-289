import click
from micro_test_hub.transports.cli.v1_0.commands.project_commands import create_project, set_active_project, list_projects, run_test, delete_project, update_project

@click.group()
def cli():
    pass

cli.add_command(create_project)
cli.add_command(update_project)
cli.add_command(set_active_project)
cli.add_command(list_projects)
cli.add_command(delete_project)
cli.add_command(run_test)


if __name__ == "__main__":
    cli()
