# coding=utf-8
import numpy as np
import pandas as pd


def _parse_price(string):
    cleaned = string.replace(' ', '')
    position = cleaned.find('РУБ.')
    final = cleaned[:position]
    try:
        final = float(final)
    except:
        final = np.nan
    return final


def parse_price(dataframe, column_name='_PRICE_'):
    func = np.vectorize(_parse_price)
    dataframe.loc[:, column_name] = func(dataframe.loc[:, column_name])
    return dataframe

if __name__ == '__main__':
    data = pd.read_csv('../champ1_train.csv')
    parse_price(data)
    print(data.head())
