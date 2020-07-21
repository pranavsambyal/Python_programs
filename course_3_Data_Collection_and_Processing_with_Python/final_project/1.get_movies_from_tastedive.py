import requests
import json


def get_movies_from_tastedive(movie):
    qry = {'q': movie, 'type': 'movies', 'limit': 5,'k':'379562-python3-QVY2EYA3'}
    base_url = 'https://tastedive.com/api/similar'
    mov = requests.get(base_url, params=qry)
    dt = json.loads(mov.text)
    print(dt)
    return dt


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_movies_from_tastedive("Bridesmaids")
print(get_movies_from_tastedive("Tony Bennett"))
get_movies_from_tastedive("Black Panther")

