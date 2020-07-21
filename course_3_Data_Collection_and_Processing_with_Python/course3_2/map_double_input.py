''' Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst'''

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
for y in lst:
    greeting_doubled=map((lambda x: 2*x),y)
    print(list(greeting_doubled))