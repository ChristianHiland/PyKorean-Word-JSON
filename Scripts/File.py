import json
from Input.words import Layout

def Write(WordOUT):
    with open(WordOUT, "w") as NewFile:
        json.dump(Layout, NewFile, indent=4)


def Read(WordOUT):
    print("Reading")