import argparse
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def simplot(input, output, column=1):
    df = pd.read_csv(input)
    df.dropna(inplace=True)
    colname = df.columns[column - 1]
    df[colname] = pd.to_numeric(df[colname])
    fig = sns.displot(df, x=colname)
    fig.savefig(output)


if __name__ == "__main__":
    # Apply the default theme
    sns.set_theme()

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    parser.add_argument("-o", "--output", help="output file", default="out.pdf")
    parser.add_argument("-c", "--column", help="input column, when using CSV", type=int)
    args = parser.parse_args()
    simplot(**vars(args))
