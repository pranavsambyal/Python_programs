'''Provided is a string saved to the variable name sentence. Split the string into a list of words,
 then create a dictionary that contains each word and the number of times it occurs. Save this
 dictionary to the variable name word_counts.'''

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
word_counts={}
words=sentence.split()
for word in  words:
    if word not in word_counts:
      word_counts[word]=1
    elif word in word_counts:
        word_counts[word]=word_counts[word]+1

print(word_counts)
