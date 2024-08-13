import typer
import os
from typing_extensions import Annotated
from .funcs import copy_whole_tree, setup_parent_dir, typer_exit_with_error_display

app = typer.Typer()

directories = ['static', 'templates']
files = ['__init__.py']

@app.command()
def create_app(name: str = typer.Argument(), boostrap: Annotated[bool, typer.Option(help="This is to setup boostrap along with app")] = False):
    try:

        if boostrap:
            print("working")
        
        setup_parent_dir(name)

        copy_whole_tree(os.path.join('templates', 'basic'), name)

    except Exception as e:
        typer_exit_with_error_display(f"Error setting up app :  {e}", exit_code=1)


if __name__ == "__main__":
    app()
