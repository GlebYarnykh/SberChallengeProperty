# coding=utf-8
import numpy as np
import pandas as pd
import nltk
import pymorphy2
import json
import requests

morph = pymorphy2.MorphAnalyzer()


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
    description = unicode(description, 'utf-8')
    tokens = nltk.wordpunct_tokenize(description)
    return tokens


def _lemmatize(word):
    global morph
    lemma = morph.parse(word)
    normalform_0 = lemma[0].normal_form
    return normalform_0


_lemmatize_list = np.vectorize(_lemmatize)


def parse_description(dataframe, column_name='_DESC_'):
    return dataframe

if __name__ == '__main__':
    data = pd.read_csv('../champ1_train.csv')
    N = 3
    test_cases = []
    tokens = []
    lemmas = []
    string = []
    for i in xrange(N):
        test_cases.append(data['_DESC_'][i])
        test_cases[i] = _correct_spelling(test_cases[i])
        tokens.append(_tokenize(test_cases[i]))
        lemmas.append(_lemmatize_list(tokens[i]))
        string.append(' '.join(lemmas[i]))
        print(string[i])
