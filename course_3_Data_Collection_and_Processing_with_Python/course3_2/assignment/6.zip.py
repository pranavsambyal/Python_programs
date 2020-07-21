'''Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the
 variable opposites if they are both longer than 3 characters each.'''
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites=filter((lambda z:len(z[0])>3 and len(z[1])>3),zip(l1,l2) )
print(list(opposites))