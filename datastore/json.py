import json
from datastore import DataStore


class JsonStore(DataStore):
    def __init__(self, filename):
        try:
            json_file = open(filename, 'r')
            self.data = json.load(json_file)
        except IOError:
            print("couldn't read json file")
            return
        except:
            print("decoding failed")
        else:
            json_file.close()

    def get_data(self, key) -> str:
        try:
            data = self.data[key]
        except KeyError:
            print("key not found!")
            return
        if isinstance(data, str):
            return data
        else:
            raise TypeError(f"key: {key} maps to invalid value")
