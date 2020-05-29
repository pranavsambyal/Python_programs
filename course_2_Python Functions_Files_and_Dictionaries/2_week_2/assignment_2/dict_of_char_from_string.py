'''Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.'''


str1 = "peter piper picked a peck of pickled peppers"
freq={}
for chars in str1:
    if chars in freq:
        freq[chars]+=1
    else:
        freq[chars]=1

print(freq)


'''Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 
and the number of times it occurs.'''


s1 = "hello"
counts={}
for chars in s1:
    if chars in counts:
        counts[chars]+=1
    else:
        counts[chars]=1
print(counts)



