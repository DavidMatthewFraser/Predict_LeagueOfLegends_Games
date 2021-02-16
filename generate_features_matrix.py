import main

def generate_feature_matrix(summoner_name):
    summoner_data = main.get_SUMMONER_V4(summoner_name)
    match_history = main.get_MATCHES_V4(summoner_data['accountId'])
    games = [(game['gameId'], game['champion']) for game in match_history['matches']]
    get = 11
    features_matrix = [['barons,', 'rifts,', 'dragons,', 'enemy_barons,', 'enemy_rifts,', 'enemy_dragons,', 'game_result']]
    for game in games:
        if get == 0: 
            break;
        get -= 1
        gameId = game[0]
        champion = game[1]
        game_stats = main.get_MATCH_V4(gameId)
        # print(str(champion) + " " + str(game_stats['gameId']))
        # Determine Which Team our player is on by using championId
        team = None
        players = game_stats['participants']
        for player in players:
            if player['championId'] == champion:
                team = player['teamId']
        #        print(team)
        teams = []
        teams.append(game_stats['teams'][int(team/100 - 1)])
        del game_stats['teams'][int(team/100 - 1)]
        teams.append(game_stats['teams'][0])
        # print(teams[0]['win'] + " " + teams[1]['win'])
        did_win = teams[0]['win']
        # Generate a feature matrix
        # player team:
        p_barons = str(teams[0]['baronKills']) + ","
        p_rifts = str(teams[0]['riftHeraldKills']) + "," 
        p_dragons = str(teams[0]['dragonKills']) + ","
        # enemy team:
        e_barons = str(teams[1]['baronKills']) + ","
        e_rifts = str(teams[1]['riftHeraldKills']) + ","
        e_dragons = str(teams[1]['dragonKills']) + "," 
        features_matrix.append([p_barons, p_rifts, p_dragons, e_barons, e_rifts, e_dragons, did_win])
    for row in range(len(features_matrix)):
        for col in range(len(features_matrix[0])):
            print(str(features_matrix[row][col]) + " ", end='')
        print('')

generate_feature_matrix('wildstein')