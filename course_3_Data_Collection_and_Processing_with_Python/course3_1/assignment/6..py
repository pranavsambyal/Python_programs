'''Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in
the ActiveCode window.'''
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1=sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2=sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3=sports['gymnastics']['women']
# Assign the string 'rings' to the name v4
v4=sports['gymnastics']['men'][3]
print(v1+' '+v2)
print(v3)
print(v4)
