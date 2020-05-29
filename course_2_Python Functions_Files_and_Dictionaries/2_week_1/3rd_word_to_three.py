f=open("school_prompt.txt",'r')
file=f.readlines()
three=[]
for x in file:
    line=x.split()
    three.append(line[2])
    print(three)
f.lose()