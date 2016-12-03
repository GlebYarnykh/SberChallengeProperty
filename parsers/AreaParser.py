# coding=utf-8
import numpy as np
import pandas as pd


def _parse_area(string):
    cleaned = string.replace(',', '.')
    position = cleaned.find('м')
    final = cleaned[:position]
    try:
        final = float(final)
    except:
        final = np.nan
    return final


def parse_area(dataframe, column_name='_AREA_'):
    func = np.vectorize(_parse_area)
    dataframe.loc[:, column_name] = func(dataframe.loc[:, column_name])
    return dataframe

if __name__ == '__main__':
    data = pd.read_csv('../champ1_train.csv')
    parse_area(data)
    print(data.head())
