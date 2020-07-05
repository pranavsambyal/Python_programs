''' Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.'''

lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check=[]
for x in range(len(lst_tups)):
    tup=lst_tups[x]
    print(tup)
    t_check.append(tup[2])
print(t_check)

""" Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple
 into a list called seconds."""
seconds=[]
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
for x in range(len(tups)):
    tup=tups[x]
    print(tup)
    seconds.append(tup[1])
print(seconds)