'''Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the
  most frequent letter based on the dictionary. Assign this letter to the variable best_char.Then, find the least
  frequent letter in the string and assign the letter to the variable worst_char.'''

sally = "sally sells sea shells by the sea shore"

characters={}
for chars in sally:
    if chars in characters:
        characters[chars]+=1
    else:
        characters[chars]=1
max_value_no=0
min_value_no=999
best_char=""
worst_char=''
for keys in characters:
    if characters[keys]>max_value_no:
        max_value_no=characters[keys]
        best_char=keys
for keys in characters:
     if characters[keys]<min_value_no:
            min_value_no=characters[keys]
            worst_char=keys

print(best_char)
print(worst_char)