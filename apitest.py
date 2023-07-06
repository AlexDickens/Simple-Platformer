import requests
import json

dataR = requests.get("https://alexasteroids.000webhostapp.com/highscore.txt")
contents = dataR.text


data1 = json.loads(contents)


username = list(data1.keys())[0]
highestscore = data1[username]


print(username)
print(highestscore)