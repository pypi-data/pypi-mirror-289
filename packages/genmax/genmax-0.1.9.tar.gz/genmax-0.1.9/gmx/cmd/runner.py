from typing import List, Optional
import typer
from gmx.logic.workflow import WorkFlowLogic

def init(
        workflows: List[str] = typer.Argument(
            ..., 
            help="List the workflows to run."
        ),
        data: Optional[str] = typer.Option(None, "--data", "-d", help="Data for the workflow files.")
    ):
    """
    Run a workflow.

    Args:
        workflows (list): List of workflows to run.
        data (str, optional): Data for the workflow files.
    """
    typer.echo("Running workflow.")
    wf = WorkFlowLogic()
    wf.run_workflows(workflows, data)