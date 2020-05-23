f=open("emotion_words.txt",'r')
file=f.readlines()
num_words=0
for x in file:
    words=x.split()
    num_words=num_words+len(words)
print(num_words)
f.close()