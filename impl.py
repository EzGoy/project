import random

from tools import readData


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
    print('Ваш результат:', res, 'из', nTerms)
    if res != nTerms:
        print('Повторить:', failedAnswers)


def runTrain():
    dataDict = readData()
    terms = list(dataDict.keys())
    random.shuffle(terms)
    for term in terms:
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