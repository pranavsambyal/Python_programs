L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]
d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
print(d)
# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))
