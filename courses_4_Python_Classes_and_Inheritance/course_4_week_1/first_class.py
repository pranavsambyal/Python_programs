'''Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2,
 which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10.
 Save this instance to a variable t'''
class NumberSet():
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
t=NumberSet(6,10)
print(t.num1)
print(t.num2)