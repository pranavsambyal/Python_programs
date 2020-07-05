file=open("tryfile.txt","w")
for no in range(1000):
    file.write("this is the {} line".format(no))
file.close()