words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
e = "d"
ed = "ed"
for x in words:
    a = len(x)

    if (x[a - 1] == "e"):
        past_tense.append(x + e)


    else:
        past_tense.append(x + ed)

print(words)
print(past_tense)
