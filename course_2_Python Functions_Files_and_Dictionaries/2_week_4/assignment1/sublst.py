'''Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to
return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches
the number 5 (it should not contain the number 5).'''

def sublist(list1):
    x = 0
    nwlt = []
    while not list1[x] == 5:
        nwlt.append(list1[x])
        print(x)
        x+=1
    return nwlt
lst=[2,7,89,3,1,5,7,3,39,7,9]
s=sublist(lst)
print(s)

