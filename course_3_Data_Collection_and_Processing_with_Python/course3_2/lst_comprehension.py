'''The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to
 accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed'''

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)
lst2=[num for num in L if num>10]
print(lst2)