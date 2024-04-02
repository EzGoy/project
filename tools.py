import json

realDataFilePath = './data/realData.json'
testDataFilePath = './data/testData.json'

def readData():
    with open(realDataFilePath, encoding="utf-8") as f:
        data = f.read()
    return json.loads(data)
