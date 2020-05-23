p_phrase = "was it a car or a cat I saw"
a_word_p=p_phrase.split()
a=""
a=a.join(a_word_p)
print(a)
r_phrase=""
for y in range(len(p_phrase)):
    r_phrase=r_phrase+p_phrase[-1-y]
print(r_phrase)
