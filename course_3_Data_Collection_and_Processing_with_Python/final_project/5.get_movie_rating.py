import requests
import json
def get_movie_data(mov):
    base_url = 'http://www.omdbapi.com/'
    pram = {'t': mov, 'r': 'json', 'apikey': '79f3ff7e'}
    web = requests.get(base_url, params=pram)
    mov_data=json.loads(web.text)
    print(mov_data)
    return mov_data
def get_movie_rating(mov_data):
    data=mov_data['Ratings']
    for provider in data:
        if provider['Source']=='Rotten Tomatoes':
            score_percent=provider['Value']
            score=int(score_percent.strip('%'))
            print(score)
            break
        else:
            score=0
    return score
print(get_movie_rating(get_movie_data('Black Panther')))
