import main
import time

total = 0
page = 1
json = main.get_LEAGUE_V4(main.tiers[3], main.divisions[2], 1) 
while(len(json) != 0):
    print(len(json))
    print(page)
    json = main.get_LEAGUE_V4(main.tiers[3], main.divisions[2], page) 
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