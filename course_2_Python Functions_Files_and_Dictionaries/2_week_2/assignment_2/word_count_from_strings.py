'''Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.'''


str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words={}
words=str1.split()
for chars in words:
    if chars in freq_words:
       freq_words[chars]+=1
    else:
        freq_words[chars]=1
print(freq_words)


'''Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you 
  have seen that word.'''

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d={}
word=sent.split()
for chars in word:
    if chars in wrd_d:
       wrd_d[chars]+=1
    else:
        wrd_d[chars]=1
print(wrd_d)




