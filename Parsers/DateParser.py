import pandas as pd
import numpy as np


def parse_date(dataframe, column_name='_DATE_'):
    dataframe.loc[:, column_name] = pd.to_datetime(dataframe.loc[:, column_name], errors='coerce')
    return

if __name__ == '__main__':
    data = pd.read_csv('../champ1_train.csv')
    parse_date(data, '_DATE_')
    print(data['_DATE_'].head())
