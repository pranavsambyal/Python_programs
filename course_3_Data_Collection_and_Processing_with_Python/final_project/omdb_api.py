import requests
import json
title='Avengers: Infinity War'
base_url='http://www.omdbapi.com/'
pram={'t':title,'r':'json','apikey':'79f3ff7e'}
web=requests.get(base_url,params=pram)
print(web.url)