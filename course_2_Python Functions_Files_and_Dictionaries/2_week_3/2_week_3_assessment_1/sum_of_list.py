'''Write a function, accum, that takes a list of integers as input and returns the sum of those integers.'''
def accum(c):
    sum=0
    for x in c:
        sum+=x
    return sum
a=[1,2,3,54,5,6]
print(accum(a))