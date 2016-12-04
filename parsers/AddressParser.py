# coding=utf-8
import json
import requests
import numpy as np


class AddressCoorsConverter(object):
    def __init__(self):
        pass

    @staticmethod
    def get_adress_info(long, lat):
        string_request = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode="
        string_request += str(long) + ',' + str(lat)
        r = requests.get(string_request)
        data = json.loads(r.content)['response']['GeoObjectCollection']["featureMember"]
        if len(data) == 5:
            street = data[0]['GeoObject']['name'].encode('utf-8')
            city = data[0]['GeoObject']['name'].encode('utf-8')
            oblast = data[2]['GeoObject']['name'].encode('utf-8')
            okrug = data[3]['GeoObject']['name'].encode('utf-8')
            return street, city, oblast, okrug
        street = data[1]['GeoObject']['name'].encode('utf-8')
        other_info_string = data[1]['GeoObject']['description'].encode('utf-8').split(', ')
        if len(other_info_string) == 3:
            city, oblast, country = other_info_string[0], other_info_string[1], other_info_string[2]
            okrug = data[-2]['GeoObject']['name'].encode('utf-8')
        else:
            city, country = other_info_string[0], other_info_string[1]
            oblast = data[-3]['GeoObject']['name'].encode('utf-8')
            okrug = data[-2]['GeoObject']['name'].encode('utf-8')
        return street, city, oblast, okrug

if __name__ == '__main__':
    parser = AddressCoorsConverter()
    street, city, oblast, okrug = parser.get_adress_info(47.24982, 56.13138)
    street, city, oblast, okrug = parser.get_adress_info(61.5924759, 54.0818634)
    street, city, oblast, okrug = parser.get_adress_info(104.3219, 52.2538872)
    street, city, oblast, okrug = parser.get_adress_info(39.4440079, 47.0912743)
    street, city, oblast, okrug = parser.get_adress_info(37.5546, 55.76212)
    street, city, oblast, okrug = parser.get_adress_info(40.0542145, 46.9761)
    street, city, oblast, okrug = parser.get_adress_info(82.82184, 55.18734)
    street, city, oblast, okrug = parser.get_adress_info(37.4478455, 55.8850937)