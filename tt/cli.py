"""Public docstring."""
import click
import os


class ComplexCLI(click.MultiCommand):
    """Allow multiple commands."""

    def list_commands(self, ctx):
        """List commands."""
        rv = []
        for filename in os.listdir(
                os.path.join(os.path.dirname(__file__), "commands")):
            if filename.endswith(".py") and not filename.startswith("__"):
                rv.append(filename.replace('.py', ''))
        
        rv.sort()
        return rv
    
    def get_command(self, ctx, cmd_name):
        """Get commands."""
        try:
            mod = __import__(f"tt.commands.{cmd_name}", 
                             None, None, ["cli"])
        except ImportError:
            return
        return mod.cli
            

@click.command(cls=ComplexCLI)
def cli():
    """Welcome to time-tracker."""
    pass
