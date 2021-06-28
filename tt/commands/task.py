"""Add task to timetracker."""
from fileinput import close
import click
from datetime import datetime

today = datetime.now()
data_location = f'tt/data/{today.day}{today.month}{today.year}'


class Task:
    """Create task."""
    
    def __init__(self, task, description):
        self.task = task
        self.time = f"{datetime.now()}"
        self.description = description
    

def file_exist(file):
    """Check if file exists."""
    try:
        open(file, 'r')
        close()
    except FileNotFoundError:
        return False
    return True
   
 
@click.group()
@click.option('-t', "--task", type=str, help="Task about to be started")
@click.option('-d', "--description", 
              type=str, help="Description of task. (optional)")
@click.pass_context
def cli(ctx, task, desc=None):
    """Add task to time tracker."""
    ctx.obj = Task(task, desc)


@cli.command()
@click.pass_context
def add(ctx):
    """Add task."""
    if file_exist(data_location):
        with open(data_location, 'a') as f:
            f.write(f"""
s,{ctx.obj.time},{ctx.obj.task},{ctx.obj.description}""")
        click.echo("Get Busy!")
    else:
        click.echo("Say hello first!")


@cli.command()
@click.pass_context
def end(ctx):
    """End current task."""
    if file_exist(data_location):
        with open(data_location, 'a') as f:
            f.write(f"""
e,{ctx.obj.time},{ctx.obj.task}""")
        click.echo("Well done.")
    else:
        click.echo("Say hello first!")
