import typer
from gmx.cmd.runner import init as init_runner
from gmx.cmd.initialize import init

app = typer.Typer()
app.command("init")(init)
app.command("run")(init_runner)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Generate code using gmx.
    """
    if ctx.invoked_subcommand is None:
        typer.echo("Welcome to Genmax!!")
        typer.echo("To explore commands at any time, type:")
        typer.echo("gmx --help")

if __name__ == "__main__":
    app()