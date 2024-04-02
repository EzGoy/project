import random

from self import self

from tools import readData

import json

realDataFilePath = './data/realData.json'
testDataFilePath = './data/testData.json'


class guide:

    def checkAnswer(self, definition, answer):
        if answer == definition:
            return True
        else:
            return False

    def prepareDefinitionOutput(self, definition):
        for i in definition:
            if i == "," or i == ".":
                definition = definition.replace(i, "")
                definition = definition.split()
                random.shuffle(definition)
                return definition

    @staticmethod
    def readData():
        with open(realDataFilePath, encoding="utf-8") as f:
            data = f.read()
        return json.loads(data)

    def runTest(self):
        dataDict = readData()
        terms = list(dataDict.keys())
        random.shuffle(terms)
        res = 0
        nTerms = len(terms)
        failedAnswers = []
        print('Начинаем тестирование')

        for term in terms:
            definition = dataDict[term]
            print(term)
            self.prepareDefinitionOutput(definition)
            ok = self.checkAnswer(definition, input())
            if ok:
                res += 1
            else:
                failedAnswers.append(term)

        print('Тестироание закончено')
        print('Ваш результат:', res, 'из', nTerms)
        if res != nTerms:
            print('Повторить:', failedAnswers)

    def runTrain(self):
        dataDict = readData()
        terms = list(dataDict.keys())
        random.shuffle(terms)
        print('Начинаем тренировку')

        for term in terms:
            definition = dataDict[term]
            while True:
                print(term)
                self.prepareDefinitionOutput(definition)
                ok = self.checkAnswer(definition, input())
                if ok:
                    print('Верно! Давай дальше')
                    break
                else:
                    print('Неправильно! Давай ещё раз')

        print('Тренировка окончена')

    def listTerms(self):
        dataDict = readData()
        terms = list(dataDict.keys())
        a = []
        for i in range(0, len(terms)):
            a.extend([terms[i], "- это", dataDict[terms[i]]])
        return a

    def __init__(self):
        self.__termsDict = readData()
