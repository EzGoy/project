import json
import random

dataFilePath = './data/example.json'


def readData():
    with open(dataFilePath, encoding="utf-8") as f:
        data = f.read()
    return json.loads(data)


def runTest():
    dataDict = readData()
    terms = list(dataDict.keys())
    random.shuffle(terms)
    res = 0
    nTerms = len(terms)
    failedAnswers = []
    for term in terms:
        print(term)
        definition = dataDict[term]
        answer = input()
        if answer == definition:
            res += 1
        else:
            failedAnswers.append(term)
    if res == nTerms:
        print('Ваш результат:', res, 'из', nTerms)
    else:
        print('Ваш результат:', res, 'из', nTerms, '\nПовторить:', failedAnswers)


def runTrain():
    dataDict = readData()
    terms = list(dataDict.keys())
    random.shuffle(terms)
    for i in range(0, len(terms)):
        term = terms[i]
        definition = dataDict[term]
        print(term)
        answer = input()
        while answer != definition:
            answer = input()


def listTerms():
    dataDict = readData()
    terms = list(dataDict.keys())
    for i in range(0, len(terms)):
        print(terms[i], "- это", dataDict[terms[i]])


if __name__ == "__main__":
    listTerms()