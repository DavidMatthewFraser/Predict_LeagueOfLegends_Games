import main

match_id = 3788372057

json = main.get_MATCH_V4(match_id)

print('Teams')
for team in json['teams']:
    main.format_response(team)
print('Participants')
for participant in json['participants']:
    main.format_response(participant)
