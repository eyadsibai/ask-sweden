import pandas as pd


def read_data():
    return pd.read_csv('data/prognos.csv', sep=';')


def get_expected_population(year):
    df = read_data()
    return df[year].sum()
