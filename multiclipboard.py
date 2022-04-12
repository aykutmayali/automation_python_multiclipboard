import sys
from textwrap import indent
import clipboard
import json


SAVED_DATA= "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:  
       json.dump(data, f)



def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) ==2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key for saving :")
        text = clipboard.paste()
        data[key] = text
        save_data(SAVED_DATA,data)
        print("Data saved!")

    elif command == "load":
        key = input("Enter a key for loading :")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("The key does not exist")

    elif command == "list":
        print(json.dumps(data, indent=4, sort_keys=True))
    else:
        print("Unknown command")

else:
    print("Please pass exactly one command.")