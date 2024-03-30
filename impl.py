import random

from tools import readData


def checkAnswer(definition, answer):
    if answer == definition:
        return True
    else:
        return False


def prepareDefinitionOutput(definition):
    for i in definition:
        if i == "," or i == ".":
            definition = definition.replace(i, "")
    definition = definition.split()
    random.shuffle(definition)
    return definition


def runTest():
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
        # print(prepareDefinitionOutput(definition))
        ok = checkAnswer(definition, input())
        if ok:
            res += 1
        else:
            failedAnswers.append(term)

    print('Тестироание закончено')
    print('Ваш результат:', res, 'из', nTerms)
    if res != nTerms:
        print('Повторить:', failedAnswers)


def runTrain():
    dataDict = readData()
    terms = list(dataDict.keys())
    random.shuffle(terms)
    print('Начинаем тренировку')

    for term in terms:
        definition = dataDict[term]
        while True:
            print(term)
            # print(prepareDefinitionOutput(definition))
            ok = checkAnswer(definition, input())
            if ok:
                print('Верно! Давай дальше')
                break
            else:
                print('Неправильно! Давай ещё раз')

    print('Тренировка окончена')


def listTerms():
    dataDict = readData()
    terms = list(dataDict.keys())
    for i in range(0, len(terms)):
        return terms[i], "- это", dataDict[terms[i]]
