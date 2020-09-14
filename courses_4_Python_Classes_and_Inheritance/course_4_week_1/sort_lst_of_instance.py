''''''
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method(sort_priority)-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("---- lambda calling sort_pirority-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)

print("---- lambda call for price-----")
for f in sorted(L, key=lambda x: x.price):
    print(f.name)
