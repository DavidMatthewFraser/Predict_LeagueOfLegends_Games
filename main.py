import requests
import time

api_key = input('api_key: ')

# Meta-Data
tiers = ['DIAMOND', 'PLATINUM', 'GOLD', 'SILVER', 'BRONZE', 'IRON']
divisions = ['I', 'II', 'III', 'IV']

# API Request URLS
SUMMONER_V4 = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
LEAGUE_V4 = 'https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/'
MATCHES_V4 = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
MATCH_V4 = 'https://na1.api.riotgames.com/lol/match/v4/matches/'

# API Request Functions
def get_SUMMONER_V4(name):
    return requests.get(SUMMONER_V4 + name + "?api_key=" + api_key).json()

def get_LEAGUE_V4(tier, division, page):
    return requests.get(LEAGUE_V4 + tier + "/" + division + "?page=" + str(page) + "&api_key=" + api_key).json()

def get_MATCHES_V4(id):
    return requests.get(MATCHES_V4 + id + "?api_key=" + api_key).json()

def get_MATCH_V4(match_id):
    return requests.get(MATCH_V4 + str(match_id) + "?api_key=" + api_key).json()

def format_response(json):
    for key,value in json.items():
        print(str(key) + ': ' + str(value))

''' 
name = 'wildstein'
json = SUMMONER_V4_by_name(name)
format_response(json)
'''



# ToDo: Make a Player Class

# NA by Default regions = ['BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'RU', 'TR1']


# Loop Through Every Page without exceeding the rate limit



