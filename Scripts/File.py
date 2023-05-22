import json

def Write(WordOUT, Layout):
    with open(WordOUT, "w") as NewFile:
        json.dump(Layout, NewFile, indent=4, ensure_ascii=False)

def Read(WordOUT):
    print("Reading")