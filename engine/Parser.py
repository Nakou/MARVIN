import json
import re

wordList = []
def parser(message):
    message = message.lower()
    message = re.sub("[^a-z0-9|\" ]","",message)
    message = message.replace("\"", "")
    message = message.replace("_", " ")
    wordList = message.split(" ")
    for c in wordList:
        print(c)
    return wordList
