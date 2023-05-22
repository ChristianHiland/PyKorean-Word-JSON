import json

def Write(WordOUT, LayoutWords):
    with open(WordOUT, "w") as NewFile:
        json.dump(Layout, NewFile, indent=4, ensure_ascii=False)
def Read(WordOUT, LanguageJSON):
    with open(LanguageJSON, "r") as CheckLanguage:
        Languages = json.load(CheckLanguage)
        print("Type one of these Languages (The words are case-sensitive) ")
        for i in Languages:
            print(i)
        UserLanguage = input("\n Language: ")
        with open(WordOUT, "r") as Words:
            Data = json.load(Words)
            text = input("Word: ")
            LowText = str(text.lower())
            theword = Data['English'][str(LowText)]
            print(str(theword))
def ReadLang(LanguageJSON):
    with open(LanguageJSON, "r") as LangJSON:
        Data = json.load(LangJSON)
        Languages = Data['Languages']
        print("Languages Installed:\n")
        for i in Languages:
            print(i)
            print("Sub-Words:\n")
            Words = Data['Languages'][i]['Words']
            Sen = Data['Languages'][i]['Sen']
            print(Words)
            print(Sen)
            print("")
def Erase(WordOUT):
    with open(WordOUT, "w") as EraseFile:
        EraseFile.write("")
def NewLang(LanguageJSON, LayoutLanguage):
    LanguageAdd = input("Did you add the language? [Y/N] ")
    if LanguageAdd.lower() == str("n"):
        print("\nYou will replace this like the same layout of the English one,\nbut the words in English you need to put them into your language.")
        print("You will need to edit the layout of the 'LayoutLanguage' in 'Input/words.py.' Then run the app again.")
    elif LanguageAdd.lower() == str("y"):
        with open(LanguageJSON, "w") as LangJSON:
            json.dump(LayoutLanguage, LangJSON, indent=4, ensure_ascii=False)
        print("Wrote to the Language JSON.")