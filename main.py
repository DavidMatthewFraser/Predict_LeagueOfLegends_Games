from Game import Game
from GameScraper import GameScraper
import time

'''
g = GameScraper
games = g.scrape('GOLD', 'III', 15)
print(games)
'''

games = [3826253208, 3830790533, 3838789616, 3835771964, 3838714937, 3827036297, 3790126273, 3813881199, 3835624253, 3816124536, 3837210814, 3832286716, 3837650146, 3804098005, 3834508606]

for game in games:
    time.sleep(100)
    g = Game(str(game))
    print(game, g.getMasteryDiff(), ',', g.getRankDiff(), ',', g.getWinrateDiff(), ',', g.getResult())
print(games)
