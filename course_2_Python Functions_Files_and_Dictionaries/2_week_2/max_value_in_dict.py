'''Create a dictionary called lett_d that keeps track of all of the characters in the string
  product and notes how many times each character was seen. Then, find the key with the highest
  value in this dictionary and assign that key to max_value.'''

product = "iphone and android phones"
lett_d={}
for chars in product:
    if chars in lett_d:
        lett_d[chars]+=1
    else:
        lett_d[chars]=1
max_value_no=0
max_value=""
for keys in lett_d:
    if lett_d[keys]>max_value_no:
        max_value_no=lett_d[keys]
        max_value=keys

print(max_value)

