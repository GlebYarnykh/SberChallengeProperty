from yandex_maps import api
api_key = 'my_api_key'

import requests
r = requests.get("https://geocode-maps.yandex.ru/1.x/?format=json&geocode=47.24982,56.13138")
json_string = r.content
# url = api.get_external_map_url(47.24982, 56.13138)
# api.get_map_url()
print 'HUY'