import pandas as pd


def read_data():
    return pd.read_csv('data/car_accidents.csv', encoding='UTF-8')


def get_num_accidents(year, city):
    df = read_data()
    year_data = df['ar'] == year
    city_data = df['kommun'] == city
    return len(df[year_data & city_data])


def get_water_usage_stockholm(year):
    df = pd.read_csv('data/water_usage_stockholm.csv')
    return df[year].sum()


def get_num_apartments_stockholm(year):
    df = pd.read_csv('data/new_built_housing.csv')
    df.loc[df.region.str.contains('Stockholm'), 'number apartments 2015'].sum()
