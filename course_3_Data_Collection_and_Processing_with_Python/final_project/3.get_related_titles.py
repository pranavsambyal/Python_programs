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
    return movies
def get_related_titles(mov_lst):
    all_movies=[]
    for mov in mov_lst:
        movies=extract_movie_titles(get_movies_from_tastedive(mov))
        for m in movies:
            if m not in all_movies:
                all_movies.append(m)
    print(all_movies)
    return all_movies

get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])




