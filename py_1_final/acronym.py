stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
ac=[]
acro=""
words=org.split()
for x in words:
    if x not in stopwords:
        ac.append(x[0].upper())
acro=acro.join(ac)
print(acro)
