f=open("school_prompt.txt",'r')
file=f.readlines()
p_words=[]
for x in file:
    y=x.split()
    for z in y:
        for n in range (len(z)):
            if z[n]=='p'or z[n]=='P':
                p_words.append(z)
                break


print(p_words)
f.close()