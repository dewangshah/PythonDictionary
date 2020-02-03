import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]

    elif len(get_close_matches(word,data.keys(),cutoff = 0.75)) >0:
        option = get_close_matches(word,data.keys(),cutoff = 0.75)[0]
        choice = input("Word not found in Dictionary, did you mean '%s' instead? Press y if Yes." % option)

        if choice.lower() == "y":
            return data[option]
        else:
            return "Word not found in Dictionary."
    else:
        return "Word not found in Dictionary."

word = input("Enter a word:")

definitions = translate(word.lower()) #Only lowercase words are present in Dictionary
if type(definitions) == str: #depending on number of meanings, definitions can be a string or a list
    print(definitions)
else:
    for item in definitions:
        print("-"+item)
