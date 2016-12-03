import json
import requests
import numpy as np

def get_adress_info(long, lat):
    string_request = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode="
    string_request += str(long) + ',' + str(lat)
    r = requests.get(string_request)
    data = json.loads(r.content)['response']['GeoObjectCollection']["featureMember"]
    try:
        street = data[1]['GeoObject']['name'].encode('utf-8')
    except:
        street = np.nan
    try:
        city = data[3]['GeoObject']['name'].encode('utf-8')
    except:
        city = np.nan
    try:
        oblast = data[5]['GeoObject']['name'].encode('utf-8')
    except:
        oblast = np.nan
    return street, city, oblast

if __name__ == '__main__':
    street, city, oblast = get_adress_info(47.24982, 56.13138)
    street, city, oblast = get_adress_info(61.5924759, 54.0818634)
    street, city, oblast = get_adress_info(104.3219, 52.2538872)