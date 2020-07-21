import requests
import json


def get_movies_from_tastedive(movie):
    qry = {'q': movie, 'type': 'movies', 'limit': 5,'k':'379562-python3-QVY2EYA3'}
    base_url = 'https://tastedive.com/api/similar'
    mov = requests.get(base_url, params=qry)
    dt = json.loads(mov.text)
    return dt

def extract_movie_titles(rt_dt):
    movies=[]
    movie_list=rt_dt['Similar']['Results']
    for data in (movie_list):
        movies.append(data['Name'])
    print(movies)
    return movies


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))




