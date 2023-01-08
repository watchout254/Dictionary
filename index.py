import json
from difflib import get_close_matches
metaData = json.load(open('dictionary_compact.json'))

print("\t\tWelcome to Jua maneno dictionary")
letter = input("Kindly type a word: ").lower()
itajipa = get_close_matches (letter, metaData.keys(),n=5)
def muks(existance):
    if existance in metaData:
        return metaData[existance]
    elif len(existance) > 0:
        mbichwa = input(f"Word not found, Kindly try these....:{itajipa}::").lower()
        return metaData[mbichwa]
    else:
       return "Sorry friend, it does not exist!!!"

print(muks(letter))