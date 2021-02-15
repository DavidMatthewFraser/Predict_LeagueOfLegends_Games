import requests
import time

api_key = 'your api key'

SUMMONER_V4 = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
LEAGUE_V4 = 'https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/'

def SUMMONER_V4_by_name(name):
    return requests.get(SUMMONER_V4 + name + "?api_key=" + api_key).json()

def get_LEAGUE_V4(tier, division, page):
    return requests.get(LEAGUE_V4 + tier + "/" + division + "?page=" + str(page) + "&api_key=" + api_key).json()


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
tiers = ['DIAMOND', 'PLATINUM', 'GOLD', 'SILVER', 'BRONZE', 'IRON']
divisions = ['I', 'II', 'III', 'IV']

# Loop Through Every Page without exceeding the rate limit
total = 0
page = 1
json = get_LEAGUE_V4(tiers[3], divisions[2], 1) 
while(len(json) != 0):
    print(len(json))
    print(page)
    json = get_LEAGUE_V4(tiers[3], divisions[2], page) 
    page += 1
    if(page % 100 == 0):
        print("sleeping")
        time.sleep(120)
    total += len(json)
    if len(json) != 0:
        for obj in json:
        # format_response(obj)
            name = obj["summonerName"]
            if(name[:4] == "wild"):
                print(name)
        # print ('====================================')
print("\n", total, page)


