import json


# d = {"Canada": [38, 24, 12],
#      "Chine": [1, 5, 8],
#      "USA": [5, 9, 4],
#      "Russie": [4, 5, 5],
#      "Autriche": [27, 25, 11],
#      "Norvege": [5, 4, 3],
#      "Finlande": [6, 8, 1],
#      "Slovenie": [18, 16, 16]}



# print(json.dumps(d))
# with open("data.json", "w") as f:
#     json.dump(d, f)

with open("data.json", "r") as f:
     d = json.load(f)
     for k, v in d.items():
          print(f"{k} => {v}")