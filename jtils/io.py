import json
import pickle

def save_json(dictionary, fp):
    with open(fp, "wb") as outfile:
        json.dump(dictionary, outfile)

def load_json(fp):
    with open(fp, "rb") as infile:
        return json.load(infile)

def pickle_obj(obj, fp):
    # open a file, where you ant to store the data
    file = open(fp, 'wb')

    # dump information to that file
    pickle.dump(obj, file)

    # close the file
    file.close()

def unpickle_obj(fp):
    # open a file, where you ant to store the data
    file = open(fp, 'rb')

    # dump information to that file
    obj = pickle.load(file)

    # close the file
    file.close()
   
    return obj