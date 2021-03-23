from ApiReader import reader
from Player import Player
from Game import Game

#p = Player('ancientdengdeng')
#print(p.getMastery(121))
#print(p.getRank())
#print(p.getWinrate())


g = Game('3836397118')
print(g.getMasteryDiff())
print(g.getRankDiff())
print(g.getWinrateDiff())
print(g.getResult())