import typer
from gmx.logic.initialize import InitializeLogic

def init():
    """
    Initialize Genmax.
    """
    typer.echo(f"Initializing Genmax...")
    il = InitializeLogic()
    il.initialize_genmax()
    typer.echo("Status : Done.")
    typer.echo("")
    typer.echo("Run the sample workflow using the below command:")
    typer.echo(f"gmx run <workflow-name>")
    typer.echo("")
    typer.echo(f"Alternatively, you can pass data to your workflow.")
    typer.echo(f"gmx run <workflow-name> --data=sample")

    