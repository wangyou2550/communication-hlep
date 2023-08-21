import json


class JSONUtil():
    @classmethod
    def readJsonFile(cls,file):
        with open(file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data