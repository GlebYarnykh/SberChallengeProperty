import parsers
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('champ1_train.csv')
    parsers.PriceParser.parse_price(data)
    print(data)
