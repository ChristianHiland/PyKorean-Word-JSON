import json
from Input import *
from Scripts import *
from os import system

# The JSON File
WordOUT = "Output/words.json"

# Making the Output JSON dicionary file.
system("./MakeJSON.sh")

# Writing the JSON.
Write(WordOUT, Layout)