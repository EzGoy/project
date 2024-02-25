import json
import random

with open('example.json', encoding="utf-8") as f:
    data = f.read()
js = json.loads(data)


def test():
    terms = list(js.keys())
    random.shuffle(terms)
    res = 0
    failedanswers = []
    for i in range(0, len(terms)):
        term = terms[i]
        definition = js[term]
        print(term)
        answer = input()
        if answer == definition:
            res += 1
        else:
            failedanswers.append(term)
    if res == len(terms):
        print('Ваш результат:', res, 'из', len(terms))
    else:
        print('Ваш результат:', res, 'из', len(terms), '\nПовторить:', failedanswers)


def training():
    terms = list(js.keys())
    random.shuffle(terms)
    for i in range(0, len(terms)):
        term = terms[i]
        definition = js[term]
        print(term)
        answer = input()
        while answer != definition:
            answer = input()


def guide():
    terms = list(js.keys())
    for i in range(0, len(terms)):
        print(terms[i], "- это", js[terms[i]])
