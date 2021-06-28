"""Public docs."""
import click
from datetime import datetime

data_location = 'tt/data/worktracker'
today = datetime.now()


def get_day():
    """Get current day."""
    return f"{today.day}/{today.month}/{today.year}"


def get_start_time():
    """Get the time at which the day starts."""
    return f"{today.hour}:{today.minute}"


@click.command()
def cli():
    """Startup command in the morning."""
    # header of each day
    header = f"Date: {get_day()}"
    
    # check if header has been placed
    with open(data_location, 'r') as read_data:
        check = read_data.read()
        check = check.split('\n')
    if header in check:
        click.echo("Goodmorning, again")
    
    # create new header
    else:
        click.echo("Goodmorning")
        with open(data_location, 'a') as data:
            data.write(f"""{header}
Wake up time: {get_start_time()}
""")
