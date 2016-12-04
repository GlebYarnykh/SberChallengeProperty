# coding=utf-8
import numpy as np
import pandas as pd
import nltk
import pymorphy2
import json
import requests

morph = pymorphy2.MorphAnalyzer()


def _to_unicode(text):
    return unicode(text, 'utf-8')


def _request_spelling(text):
    params = {'text': text,
              'lang': 'ru',
              'options': 783,
              }
    response = requests.get('http://speller.yandex.net/services/spellservice.json/checkText', params=params)
    return response


def _correct_spelling(text):
    response = _request_spelling(text)
    rj = response.json()
    num_errors = len(rj)
    if response.status_code == 200:
        if num_errors > 0:
            for i in xrange(num_errors):
                error = rj[i]
                if error[u'code'] == 1:
                    suggestions = [v for v in error[u's']]
                    if suggestions:
                        suggestion = suggestions[0]
                        start = error[u'pos']
                        end = start + error[u'len']
                        text = text[:start] + text[start:end].replace(error[u'word'], suggestion) + text[end:]
                if error[u'code'] == 2:
                    start = error[u'pos']
                    end = start + error[u'len']
                    text = text[:(start-1)] + text[end:]
                if error[u'code'] == 4:
                    pass
    return text


def _tokenize(description):
    tokens = nltk.wordpunct_tokenize(description)
    return tokens


def _lemmatize(word):
    global morph
    lemma = morph.parse(word)
    normalform_0 = lemma[0].normal_form
    return normalform_0


_lemmatize_list = np.vectorize(_lemmatize)


def _parse_descripton(text):
    text = _to_unicode(text)
    text = _correct_spelling(text)
    tokens = _tokenize(text)
    lemmas = _lemmatize_list(tokens)
    final = ' '.join(lemmas)
    return final


def parse_description(dataframe, column_name='_DESC_'):
    func = np.vectorize(_parse_descripton)
    dataframe.loc[:, column_name] = func(dataframe.loc[:, column_name])
    return dataframe

if __name__ == '__main__':
    data = pd.read_csv('../champ1_train.csv')
    subset = data.iloc[:10, :]
    result = parse_description(subset)
    print(result.head())
