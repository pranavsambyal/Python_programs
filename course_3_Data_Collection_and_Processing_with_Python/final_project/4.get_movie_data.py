import requests
import json
def get_movie_data(mov):
    base_url = 'http://www.omdbapi.com/'
    pram = {'t': mov, 'r': 'json', 'apikey': '79f3ff7e'}
    web = requests.get(base_url, params=pram)
    mov_dict=json.loads(web.text)
    print(mov_dict)
    return mov_dict
get_movie_data('Black Panther')
