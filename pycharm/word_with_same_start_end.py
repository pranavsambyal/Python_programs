sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
a=sentence.split()
same_letter_count=0
for x in a:
    if(x[0]==x[-1]):
        same_letter_count+=1

print(same_letter_count)

