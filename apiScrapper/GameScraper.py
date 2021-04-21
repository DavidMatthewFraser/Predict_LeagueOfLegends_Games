from requests.models import parse_url
from ApiReader import reader
import apiKey

class GameScraper:
    def scrape(tier, division, numberOfGames):
            print('Scraping games ......')
            games = []
            # get list of players from the subset of players in the given rank
            response = reader.get_LEAGUE_V4(tier, division, numberOfGames, apiKey.key)
            # for each player, put their last game played in the games set    
            for i in range(numberOfGames):
                # ith player from the top of the list
                try:
                    summoner = response[i]['summonerName']
                    accountId = reader.get_SUMMONER_V4(summoner, apiKey.key)['accountId']
                    match = reader.get_MATCHES_V4(accountId, apiKey.key)
                    for j in range(10):
                        # last game that player played
                        games.append(match['matches'][j]['gameId'])
                    print('10 games scrapped')
                except:
                    continue;
            return games