import random
import json
import requests


## Request a word from https://random-word-api.herokuapp.com/word 
## store the word in variable: wordPickedFromURL

def getWordFromAPI():
        lenOfWord = random.randint(2, 8)
        url = f'https://random-word-api.herokuapp.com/word?length={lenOfWord}'
        wordURLResponse = requests.get(url)
        wordData = wordURLResponse.json()
        wordPickedFromURL = wordData[0]
        return wordPickedFromURL.lower()




def convertWordToSecret(realWord):
    hiddenWord = []
    for x in range(len(realWord)):
        hiddenWord.append("_")
    return hiddenWord

