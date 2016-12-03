# coding=utf-8
import numpy as np
import pandas as pd


def _type_to_category(dataframe, column_name):
    dataframe.loc[:, column_name] = dataframe[column_name].astype('category')
    return dataframe


def _one_hot_type(dataframe, column_name):
    dataframe = pd.get_dummies(dataframe, prefix=column_name, prefix_sep='', dummy_na=True, columns=[column_name], drop_first=True)
    return dataframe


def parse_type(dataframe, column_name='_TYPE_'):
    _type_to_category(dataframe, column_name)
    dataframe = _one_hot_type(dataframe, column_name)
    return dataframe

if __name__ == '__main__':
    data = pd.read_csv('../champ1_train.csv')
    data = parse_type(data)
    print(data.head())
