class Game:
    def __init__(self, gameId):
        self.gameId = gameId
        self.__initPlayers()
        self.__calcMastery()
        self.__calcRank()
        self.__calcWinrate()
    # read game data and calculate mastery, rank, winrate 
    def __initPlayers(self):
        print('initPlayers')
    def __calcMastery(self):
        print('calcMastery')
        self.masteryDiff = 1
    def __calcRank(self):
        print('calcRank')
        self.rankDiff = 2
    def __calcWinrate(self):
        print('calcWinrate')
        self.winrateDiff = 3
    def __calcResult(self):
        self.didWin = true;
    # getters for mastery, rank, wiratte, game result
    def getMasteryDiff(self):
        return self.masteryDiff
    def getRankDiff(self):
        return self.rankDiff
    def getWinrateDiff(self):
        return self.winrateDiff
    def getResult(self):
        return self.didWin
    