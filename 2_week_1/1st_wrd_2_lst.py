f=open("emotion_words.txt",'r')
file=f.readlines()

emotions=[]
num_words=0
for x in file:
    y=x.split()
    emotions.append(y[0])
print(emotions)
f.close()