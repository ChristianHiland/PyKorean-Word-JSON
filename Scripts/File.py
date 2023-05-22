import json

def Write(WordOUT, Layout):
    with open(WordOUT, "w") as NewFile:
        json.dump(Layout, NewFile, indent=4, ensure_ascii=False)
def Read(WordOUT):
    with open(WordOUT, "r") as Words:
        Data = json.load(Words)
        text = input("Word: ")
        LowText = str(text.lower())
        theword = Data['English'][str(LowText)]
        print(str(theword))
def Erase(WordOUT):
    with open(WordOUT, "w") as EraseFile:
        EraseFile.write("")
def NewLang(WordOUT):
    with open(WordOUT, "r") as Language:
        Data = json.load(Language)
        HowTo = Data['Other Languages']['Language']
        print(HowTo)
    