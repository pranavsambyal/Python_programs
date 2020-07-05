'''. Write a function named intro that takes a string as input. Given the string “Becky” as input, the function
should return: “Hello, my name is Becky and I love SI 106.”'''

def intro(x):
    y="Hello, my name is {} and I love SI 106".format(x)
    return y
a="Becky"
intro(a)