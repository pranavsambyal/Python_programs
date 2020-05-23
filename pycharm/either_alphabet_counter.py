sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
a = sentence.split()
num_a_or_e=0
for x in a:
    if (('a' in x) or ('e' in x)):
        num_a_or_e+=1
print(num_a_or_e)