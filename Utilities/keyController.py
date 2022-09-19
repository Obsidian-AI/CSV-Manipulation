import json

class keyController:
    def __init__(self):
        pass

    def getConfigKey(self, key):
        """
        Pulls values from the json settings file
        """

        try:
            with open("config.json", "r") as jsonfile:
                data = json.load(jsonfile)
            return data[key]
        except Exception as e:
            print("[-] Error Occured Loading Settings File")