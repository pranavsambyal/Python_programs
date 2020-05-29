'''Create a dictionary called char_d from the string stri, so that the key is a character
 and the value is how many times it occurs'''

stri = "what can I do"
char_d={}
for word  in  stri :
    for character in  word:
        if character not in char_d:
            char_d[character]=1
        elif character in char_d:
            char_d[character]+=1
print(char_d)