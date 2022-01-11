import json

#Ovo ispod je jedan nacin
with open("data.json", "r") as f1:
    data = json.load(f1)
    #print(data)

#Ovo je drugi nacin
data = json.load(open("data.json", "r"))
#print(data["rain"])

