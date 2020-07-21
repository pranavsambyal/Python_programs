import  requests
import json
base_url='https://tastedive.com/api/similar'
qury='pulp fiction'
parms={'q': qury,'type':'movies','k':'379562-python3-QVY2EYA3','info':1}
a=requests.get(base_url,params=parms)
b=json.loads(a.text)
print(json.dumps(b,indent=2))