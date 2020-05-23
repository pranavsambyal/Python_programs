f=open("school_prompt.txt",'r')
file=f.read()
num_lines=len(file)
beginning_chars=file[:29]
print(beginning_chars)
f.close()