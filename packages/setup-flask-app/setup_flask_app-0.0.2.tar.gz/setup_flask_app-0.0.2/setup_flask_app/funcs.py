import typer
import os
import shutil

def typer_exit_with_error_display(err, exit_code=0):
        typer.echo(err)
        typer.Exit(code=exit_code)

def setup_parent_dir(parent_dir):
    try:
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
    except OSError as err:
         typer_exit_with_error_display(f"The directory with name {parent_dir} already exists. Exit with error {err}", 1)

def copy_whole_tree(source, destination): 
     try:
        if not os.path.exists(destination):
            os.makedirs(destination)  

        for item in os.listdir(source):
            item_source = os.path.join(source, item)
            item_destination = os.path.join(destination, item)

            if os.path.isdir(item_source):
                copy_whole_tree(item_source, item_destination)
                
            else:
                shutil.copy2(item_source, item_destination)
     except Exception as err:
            typer_exit_with_error_display(f"Something went wrong. Error is: {err}", exit_code=1)