class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1)) + ("--"*(int(self.x) -1)) +'-'+ self.printed_rep
                rows.append(special_row)
            else:
                if(self.y)>(j+1):
                    rows.append(str((j+1)) + ("  "*(int(self.x) -1)) +' '+ '|')
                else:
                    rows.append(str((j + 1)) + ("  " * (int(self.x) - 1)) + ' ' + ' ')
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i)+' '
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(3, 3)
p2 = Point(4, 2)
print(p1.graph())
print()
print(p2.graph())
