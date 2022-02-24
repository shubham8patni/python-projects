import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"

# data =  clipboard.paste()
# adj1 = input("adjective1: ")
# clipboard.copy('abc')
# abc

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
    

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == 'save':
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved")
    elif command == 'load':
        key = input("Enter the Key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
    elif command == 'list':
        print(data)
    else:
        print("Unknown Command")  
else:
    print("Please pass exactly 1 command")

