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
        # self.__calcWinrate()
        self.__calcResult()

    def __initPlayers(self):
        for p in self.gameData['participantIdentities']:
            newPlayer = Player(p['player']['summonerId'])
            self.players.append([newPlayer, 'champion they played'])
        for i in range(10):
            self.players[i][1] = self.gameData['participants'][i]['championId']

    def __calcMastery(self):
        av1 = 0
        av2 = 0
        for i in range(0,5):
            av1 += self.players[i][0].getMastery(self.players[i][1])
        for i in range(5,10):
            av2 += self.players[i][0].getMastery(self.players[i][1])
        self.masteryDiff = (av1 / 5) - (av2 / 5)

    def __calcRank(self):
        av1 = 0
        av2 = 0
        ranked1 = 0
        ranked2 = 0
        for i in range(0,5):
            rank = self.players[i][0].getRank()
            if rank > 0: 
                ranked1 += 1
                av1 += rank
        for i in range(5,10):
            rank = self.players[i][0].getRank()
            if rank > 0: 
                ranked2 += 1
                av2 += rank
        self.rankDiff = (av1/ranked1) - (av2/ranked2) 

    def __calcResult(self):
        self.didWin = self.gameData['teams'][0]['win'] == 'Win'

# calculating winrate uses too many api requests
#    def __calcWinrate(self):
#        wd = 0
#        for i in range(0,5):
#            wd += self.players[i][0].getWinrate()
#        for i in range(5,10):
#            wd -= self.players[i][0].getWinrate()
#        self.winrateDiff = wd

    def getMasteryDiff(self):
        return self.masteryDiff

    def getRankDiff(self):
        return self.rankDiff

    def getResult(self):
        if(self.didWin):
            return 1
        else:
            return 0

#    def getWinrateDiff(self):
#        return self.winrateDiff

