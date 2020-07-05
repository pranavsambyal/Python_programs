'''Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to
 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”'''
def length(c):
    if len(c)>=5:
        return 'Longer than 5'
    else:
        return 'Less than 5'
a=[12,121,324,221,424,424,2,455,67,7,5,4]
print(length(a))

