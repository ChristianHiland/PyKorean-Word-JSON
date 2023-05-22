import json
from Input import wordsEnglish, wordsEnglishSen

# The Layout of the dicionary.
Layout = {
    "English": {
        wordsEnglish
    },
    "EnglishSen": {
        wordsEnglishSen
    }
}


def Write(WordOUT):
    with open(WordOUT, "w") as NewFile:
        json.dump(Layout, NewFile, indent=4)


def Read(WordOUT):
    print("Reading")