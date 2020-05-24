import sys
import click
import logging
import pandas as pd
import matplotlib.pyplot as plt


@click.command()
@click.option("--debug", "-d", is_flag=True, default=False)
@click.option("--offset", "-o", is_flag=True, default=False)
@click.option("--type", "-t", type=click.Choice(["q2c", "q2d", "d2c"]))
@click.argument("infile")
@click.argument("outfile")
def cli(debug, offset, type, infile, outfile):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    df = pd.read_csv(infile, sep=" ", names=["time", "latency"])

    if offset:
        start = df["time"][0]
        df["time"] -= start

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(df["time"] - df["time"][0], df["latency"], c="red", alpha=0.2)

    _, top = ax.get_ylim()
    ax.set_ylim(0, top)

    title_str = None
    if type == 'q2d':
        title_str = 'Queue (Q) To Issue (D)'
    elif type == 'd2c':
        title_str = 'Issue (D) To Complete (C)'
    elif type == 'q2c':
        title_str = 'Queue (Q) To Complete (C)'
    ax.set_title(title_str)
    ax.set_xlabel("Runtime (seconds)")
    ax.set_ylabel("Latency (seconds)")

    plt.subplots_adjust(left=0.15)
    plt.savefig(outfile)
