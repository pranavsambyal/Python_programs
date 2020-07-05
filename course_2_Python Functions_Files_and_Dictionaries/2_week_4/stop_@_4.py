'''Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each
 number to a new list until the number 4 appears. The function should return the new list.'''

def stop_at_four(list1):
    x = 0
    nwlt = []
    while not list1[x] == 4:
        nwlt.append(list1[x])
        x+=1
    return nwlt
lst=[2,7,89,3,1,7,3,3,4,8,6,7,1,9,7,9]
s=stop_at_four(lst)
print(s)




