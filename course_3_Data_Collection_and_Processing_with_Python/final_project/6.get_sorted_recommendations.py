import requests
import json


def get_movies_from_tastedive(movie):
    qry = {'q': movie, 'type': 'movies', 'limit': 5,'k':'379562-python3-QVY2EYA3'}
    base_url = 'https://tastedive.com/api/similar'
    mov = requests.get(base_url, params=qry)
    dt = json.loads(mov.text)
    return dt


def extract_movie_titles(rt_dt):
    movies = []
    movie_list = rt_dt['Similar']['Results']
    for data in (movie_list):
        movies.append(data['Name'])
    return movies


def get_related_titles(mov_lst):
    all_movies = []
    for mov in mov_lst:
        movies = extract_movie_titles(get_movies_from_tastedive(mov))
        for m in movies:
            if m not in all_movies:
                all_movies.append(m)
    return all_movies


def get_movie_data(mov):
    base_url = 'http://www.omdbapi.com/'
    pram = {'t': mov, 'r': 'json', 'apikey': '79f3ff7e'}
    web = requests.get(base_url, params=pram)
    mov_dict = json.loads(web.text)
    return mov_dict


def get_movie_rating(mov_data):
    data = mov_data['Ratings']
    for provider in data:
        if provider['Source'] == 'Rotten Tomatoes':
            score_percent = provider['Value']
            score = int(score_percent.strip('%'))
            print(str(score)+mov_data['Title'])
            break
        else:
            score = 0
    return score

def get_sorted_recommendations(movies_lst):
    movies=[]
    for each_movie in movies_lst:
        suggested=get_related_titles(each_movie)
        for movie in suggested:
            if movie not in movies:
                movies.append(movie)
    print(movies)
    moviee=sorted(movies,key=lambda x:(get_movie_rating(get_movie_data(x)),x),reverse=1)
    print(moviee)
    return moviee
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])




# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

