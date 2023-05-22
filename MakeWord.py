import json
from Input import *
from Scripts import *
from os import system

# The JSON File
WordOUT = "Output/words.json"

# Making the Output JSON dicionary file.
print("Making the 'words.json' file in the Output folder.")
system("./MakeJSON.sh")

# Writing the JSON.
print("Writing to the JSON file")
Write(WordOUT, Layout)
print("Done writing to the JSON file")