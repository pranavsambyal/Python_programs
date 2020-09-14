'''Part A: WOFPlayer
We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer. Every instance of WOFPlayer has three instance variables:
.name: The name of the player (should be passed into the constructor)
.prizeMoney: The amount of prize money for this player (an integer, initialized to 0)
.prizes: The prizes this player has won so far (a list, initialized to [])

Of these instance variables, only name should be passed into the constructor.
It should also have the following methods (note: we will exclude self in our descriptions):
.addMoney(amt): Add amt to self.prizeMoney
.goBankrupt(): Set self.prizeMoney to 0
.addPrize(prize): Append prize to self.prizes
.__str__(): Returns the player’s name and prize money in the following format:

Steve ($1800) (for a player with instance variables .name == 'Steve' and prizeMoney == 1800)'''

class WOFPlayer():
    def __init__(self,name):
        self.name=name
        self.prizeMoney=0
        self.prizes=[]
    def addMoney(self,amt):
        self.prizeMoney+=amt
    def goBankrupt(self):
        self.prizeMoney=0
    def addPrize(self,prize):
        self.prizes.append(prize)
    def __str__(self):
        return '{} (${})'.format(self.name,self.prizeMoney)
