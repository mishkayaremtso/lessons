import json

filename = "players.txt"
fileopen = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName': "Petya",
    'Score': 312,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Kek",
    'Score': 334,
    'awards': ["WF", "TX", "MI"]
}


myplayers = []
myplayers.append(player1)
myplayers.append(player2)


json.dump(myplayers, fileopen)
fileopen.close()


fileopen = open(filename, mode='r', encoding='Latin-1')

json_data = json.load(fileopen)

for user in json_data:
    print("Player name is: " + str(user['PlayerName']))
    print("Player score is: " + str(user['Score']))
    print("Player award 1: " + str(user['awards'][0]))
    print("Player award 2: " + str(user['awards'][1]))
    print("Player award 3: " + str(user['awards'][2]))