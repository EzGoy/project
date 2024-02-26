import json

dataFilePath = './data/example.json'


def readData():
    with open(dataFilePath, encoding="utf-8") as f:
        data = f.read()
    return json.loads(data)
