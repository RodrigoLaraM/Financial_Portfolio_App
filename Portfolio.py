import pandas as pd


def extractor():
    file = pd.read_csv("Portfolio.csv")
    return file
