import apiKey
from ApiReader import reader
class Player:
    def __init__(self, name):
        self.name=name
        self.id = reader.get_SUMMONER_V4(self.name, apiKey.key)['id'] 
    def getMastery(self, championId):
        print(reader.get_CHAMPION_MASTERY_V4(self.id, championId, apiKey.key)['championPoints'])
    def getRank():
        print('rank')
    def getWinrate():
        print('winrate')