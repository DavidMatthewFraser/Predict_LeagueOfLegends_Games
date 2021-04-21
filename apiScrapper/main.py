from Game import Game
from GameScraper import GameScraper


g = GameScraper
games = g.scrape('SILVER', 'III', 10)
print(games)
for game in games:
    # time.sleep(100)
    try:
        g = Game(str(game))
        print(game, g.getMasteryDiff(), ',', g.getRankDiff(), ',', g.getResult())
    except:
        continue
    # print games in comma separated format
