'''Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops
once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.'''

def check_nums(list1):
    x = 0
    nwlt = []
    while not list1[x] == 7:
        nwlt.append(list1[x])
        x+=1
    return nwlt
lst=[2,7,89,3,1,7,3,3,4,8,6,7,1,9,7,9]
s=check_nums(lst)
print(s)
