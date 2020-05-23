import sys
import click

@click.command()
@click.option("--verbose", "-v", is_flag=True, default=False)
def cli(verbose):
    if verbose:
        print("Hello World.")
