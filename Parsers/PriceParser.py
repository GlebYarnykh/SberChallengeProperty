import numpy as np


def parse_price(string):
    cleaned = string.replace(' ', '')
    position = cleaned.find('РУБ.')
    final = cleaned[:position]
    try:
        final = int(final)
    except:
        final = np.nan
    return final