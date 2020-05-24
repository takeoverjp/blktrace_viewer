import sys
import click
import logging
import pandas as pd
import matplotlib.pyplot as plt


@click.command()
@click.option("--debug", "-d", is_flag=True, default=False)
@click.option("--offset", is_flag=True, default=True)
@click.argument("infile")
@click.argument("outfile")
def cli(debug, offset, infile, outfile):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    df = pd.read_csv(infile, sep=" ", names=["time", "latency"])

    if offset:
        start = df["time"][0]
        df["time"] -= start

    plt.scatter(df["time"] - df["time"][0], df["latency"], c="red", alpha=0.2)
    plt.savefig(outfile)
