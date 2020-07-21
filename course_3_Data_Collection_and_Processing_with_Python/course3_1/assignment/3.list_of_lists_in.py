'''Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode
 window for further directions.'''

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1='hola' in L

# Test if [5, 8, 7] is in the list L. Save to variable name test2
n=[5, 8, 7]
test2= n in L

# Test if 6.6 is in the third element of list L. Save to variable name test3
test3=6.6 in L[2]
print(test1)
print(test2)
print(test3)