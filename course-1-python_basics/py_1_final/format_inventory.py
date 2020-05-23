inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
item=[]
nos=[]
cost=[]
for x in inventory:
    a=x.split(",")
    item.append(a[0])
    nos.append(a[1])
    cost.append(a[2])
for x in range(len(item)):
    print("The store has {} {}, each for {} USD.".format(nos[x],item[x],cost[x]))