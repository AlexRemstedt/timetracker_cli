"""Public docs."""
import click
from datetime import datetime

today = datetime.now()
data_location = f'tt/data/{today.day}{today.month}{today.year}'
user = "Alex Remstedt"


def get_day():
    """Get current day."""
    return f"{today.strftime('%d/%m/%Y')}"


def get_start_time():
    """Get the time at which the day starts."""
    return f"{today.strftime('%H:%M:%S')}"


@click.command()
def cli():
    """Startup command in the morning."""
    # header of each day
    header = f"Date: {today.strftime('%A')} {get_day()}"
    
    try:
        open(data_location, 'r')
        click.echo("Goodmorning, again!")
    except FileNotFoundError:
        click.echo("Goodmorning")
        with open(f'{data_location}', 'w') as data:
            data.write(f"""{header}
Wake up time - {get_start_time()}
{user}

  Time                       Task,Description  
---------------------------------------------""")
