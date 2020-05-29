''' Create a dictionary called d that keeps track of all the characters in the string placement and
    notes how many times each character was seen. Then, find the key with the lowest value in this
    dictionary and assign that key to min_value'''


placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d={}
for chars in placement:
    if chars in d:
        d[chars]+=1
    else:
        d[chars]=1
min_value_no=999
min_value=""
for keys in d:
    if d[keys]<min_value_no:
        min_value_no=d[keys]
        min_value=keys

print(min_value)

