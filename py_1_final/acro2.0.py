stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
ac=[]
acro="."
words=sent.split()
for x in words:
    if x not in stopwords:
        ac.append(x[0].upper()+x[1].upper())
acro=acro.join(ac)
print(acro)