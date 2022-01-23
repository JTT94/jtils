import json

def save_json(dictionary, fp):
    with open(fp, "w") as outfile:
        json.dump(dictionary, outfile)