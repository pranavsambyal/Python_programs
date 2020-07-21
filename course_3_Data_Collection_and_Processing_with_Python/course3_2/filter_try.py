# Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing=filter((lambda x:'w'in x),lst_check)
print(list(filter_testing))