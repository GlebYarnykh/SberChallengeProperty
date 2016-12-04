# coding=utf-8
import numpy as np
import pandas as pd
import nltk
import pymorphy2
morph = pymorphy2.MorphAnalyzer()


def _tokenize(description):
    description = unicode(description, 'utf-8')
    tokens = nltk.wordpunct_tokenize(description)
    return tokens


def _lemmatize(word):
    global morph
    lemma = morph.parse(word)
    print(lemma)
    normalform = lemma[0].normal_form
    return normalform


def parse_description(dataframe, column_name='_DESC_'):
    return dataframe

if __name__ == '__main__':
    data = pd.read_csv('../champ1_train.csv')
    test_case = data['_DESC_'][1]
    tokens = _tokenize(test_case)
    lemmas = _lemmatize(u'парковочных')
    print(lemmas)
