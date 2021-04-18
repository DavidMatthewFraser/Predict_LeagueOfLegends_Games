import requests
import time

class ApiReader:
    def __init__(self):
        self.numRequests = 1

    def _updateRequests(self):
        if self.numRequests > 90:
            time.sleep(120)
            self.numRequests = 0
        else:
            self.numRequests += 1

    def get_SUMMONER_V4(self,name, api_key):
        self._updateRequests()
        SUMMONER_V4 = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
        return requests.get(SUMMONER_V4 + name + "?api_key=" + api_key).json()
    
    def get_SUMMONER_BYID_V4(self, pid, api_key):
        self._updateRequests()
        SUMMONER_V4 = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/'
        return requests.get(SUMMONER_V4 + pid + "?api_key=" + api_key).json()

    def get_LEAGUE_V4(self, tier, division, page, api_key):
        self._updateRequests()
        LEAGUE_V4 = 'https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/'
        return requests.get(LEAGUE_V4 + tier + "/" + division + "?page=" + str(page) + "&api_key=" + api_key).json()
    
    def get_SUMMONER_LEAGUE_V4(self, summoner_id, api_key):
        self._updateRequests()
        LEAGUE_V4 = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
        return(requests.get(LEAGUE_V4 + summoner_id + "?api_key=" + api_key).json())

    def get_MATCHES_V4(self, pid, api_key):
        self._updateRequests()
        MATCHES_V4 = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
        print('pid: ', pid, ' ', type(pid))
        return requests.get(MATCHES_V4 + pid + "?api_key=" + api_key).json()

    def get_MATCH_V4(self, match_id, api_key):
        self._updateRequests()
        MATCH_V4 = 'https://na1.api.riotgames.com/lol/match/v4/matches/'
        return requests.get(MATCH_V4 + str(match_id) + "?api_key=" + api_key).json()

    def get_CHAMPION_MASTERY_V4(self, summoner_id, champion_id, api_key):
        self._updateRequests()
        CHAMPION_MASTERY_V4 = 'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/'
        return requests.get(CHAMPION_MASTERY_V4 + str(summoner_id) +'/by-champion/' + str(champion_id) + "?api_key=" + api_key).json()

reader = ApiReader()