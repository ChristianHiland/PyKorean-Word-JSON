from Input import *
from Scripts import *
from os import system, path

# The JSON File
WordOUT = "Output/words.json"
LanguageJSON = "Output/Language.json"
CheckFile = path.isfile(WordOUT)

if CheckFile == False:
    # Making the Output JSON dicionary file.
    print("Making the 'words.json' file in the Output folder.")
    system("./MakeJSON.sh")

UserOP = input("Do you want to Read, Write, Erase, Read a added Language, or Add a Language? [R/W/E/RL/N] ")
if UserOP.lower() == str("w"):
    # Writing the JSON.
    print("Writing to the JSON file")
    Write(WordOUT, Layout)
    print("Done writing to the JSON file")
elif UserOP.lower() == str("r"):
    # Reading the JSOn
    Read(WordOUT, LanguageJSON)
elif UserOP.lower() == str("e"):
    print("Erasing the JSON file")
    Erase(WordOUT)
elif UserOP.lower() == str("n"):
    NewLang(LanguageJSON, LayoutLanguage)
elif UserOP.lower() == str("rl"):
    ReadLang(LanguageJSON)