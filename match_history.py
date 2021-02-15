import main
def match_history():
    id = '_PoKxxf7IFMuttLdNBg9WX4hfdO9yZ-F1ALzPU65itxV61Y'
    games = main.get_MATCHES_V4(id)
    for game in games['matches']:
        main.format_response(game)
        print('=================')
match_history()

