import pandas as pd
import numpy as np


def parse_dates(data):
    data.loc[:,'_DATE_'] = pd.to_datetime(data,coerce=True)
    return