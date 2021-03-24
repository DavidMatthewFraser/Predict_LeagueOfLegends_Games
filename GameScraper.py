from requests.models import parse_url
from ApiReader import reader
import apiKey

class GameScraper:
    def scrape(tier, division, numberOfGames):
            print('Scraping games ......')
            games = []
            response = reader.get_LEAGUE_V4(tier, division, numberOfGames, apiKey.key)
            for i in range(numberOfGames):
                summoner = response[i]['summonerName']
                accountId = reader.get_SUMMONER_V4(summoner, apiKey.key)['accountId']
                match = reader.get_MATCHES_V4(accountId, apiKey.key)
                games.append(match['matches'][i]['gameId'])
            return games