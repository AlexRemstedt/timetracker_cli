"""Public docs."""
import click
import time

data_location = 'tt/data/worktracker'


def get_day():
    """Get current day."""
    today = time.localtime(time.time())
    return f"{today.tm_mday}/{today.tm_mon}/{today.tm_year}"


@click.command()
def cli():
    """Startup command in the morning."""
    # header of each day
    header = f"Date: {get_day()}"
    
    
    # check if header has been placed
    with open(data_location, 'r') as read_data:
        check = read_data.readlines()
    if header in check:
        click.echo("Goodmorning, again")
    
    # create new header
    else:
        click.echo("Goodmorning")
        with open(data_location, 'a') as data:
            data.write(header)
