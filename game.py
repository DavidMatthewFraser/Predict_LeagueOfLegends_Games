from ApiReader import reader
from Player import Player
import apiKey

class Game:
    def __init__(self, gameId):
        self.gameId = gameId
        self.gameData =  reader.get_MATCH_V4(gameId, apiKey.key)
        self.players = []
        self.__initPlayers()
        self.__calcMastery()
        self.__calcRank()
        self.__calcWinrate()
        self.__calcResult()

    def __initPlayers(self):
        for p in self.gameData['participantIdentities']:
            newPlayer = Player(p['player']['summonerId'])
            self.players.append([newPlayer, 'champion they played'])
        for i in range(10):
            self.players[i][1] = self.gameData['participants'][i]['championId']

    def __calcMastery(self):
        md = 0
        for i in range(0,5):
            md += self.players[i][0].getMastery(self.players[i][1])
        for i in range(5,10):
            md -= self.players[i][0].getMastery(self.players[i][1])
        self.masteryDiff = md

    def __calcRank(self):
        rd = 0
        for i in range(0,5):
            rd += self.players[i][0].getRank()
        for i in range(5,10):
            rd -= self.players[i][0].getRank()
        self.rankDiff = rd 

    def __calcWinrate(self):
        wd = 0
        for i in range(0,5):
            wd += self.players[i][0].getWinrate()
        for i in range(5,10):
            wd -= self.players[i][0].getWinrate()
        self.winrateDiff = wd

    def __calcResult(self):
        self.didWin = self.gameData['teams'][0]['win'] == 'Win'

    def getMasteryDiff(self):
        return self.masteryDiff

    def getRankDiff(self):
        return self.rankDiff

    def getWinrateDiff(self):
        return self.winrateDiff

    def getResult(self):
        return self.didWin