'''Write a function named total that takes a list of integers as input, and returns the total value of all
those integers added together.'''

def total(x):
    tot=0
    for y in range(len(x)):
        tot=tot+x[y]
    return tot
c=[1,4,5,5,5,5,]
tota=total(c)
print(tota)