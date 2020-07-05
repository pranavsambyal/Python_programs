s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a', 'e', 'i', 'o', 'u']
a = s.split()
num_vowels = 0
for x in a:

    for y in vowels:

        if (y in x):
            num_vowels += x.count(y)

print(num_vowels)
