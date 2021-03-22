import apiKey
from ApiReader import reader
class Player:
    def __init__(self, name):
        self.name=name
        self.id = reader.get_SUMMONER_V4(self.name, apiKey.key)['id'] 
    def getMastery(self, championId):
        print(reader.get_CHAMPION_MASTERY_V4(self.id, championId, apiKey.key)['championPoints'])
    def getRank(self):
        response = reader.get_SUMMONER_LEAGUE_V4(self.id, apiKey.key)
        tiers = {'DIAMOND' : 6, 'PLATINUM': 5, 'GOLD': 4, 'SILVER': 3, 'BRONZE': 2, 'IRON': 1}
        divisions = {'I': (4/5), 'II': (3/5), 'III': (2/5), 'IV': (1/5)}
        rank = 0
        for queueType in response:
            tier = queueType['tier']
            division = queueType['rank']
            lp = queueType['leaguePoints']
            rank = max(rank, tiers[tier] + divisions[division] + (lp * (1/5) / 100))
        print(rank)
    def getWinrate():
        print('winrate')