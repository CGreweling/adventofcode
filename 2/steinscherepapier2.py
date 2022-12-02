#!/bin/python



f = open("plays.txt", "r")

scores={'A X' : 4,
'A Y' : 8,
'A Z' : 3,
'B X' : 1,
'B Y' : 5,
'B Z' : 9,
'C X' : 7,
'C Y' : 2,
'C Z' : 6}

windrawlosetranslate= {
    'A X' : 'A Z',
    'A Z' : 'A Y',
    'A Y' : 'A X',
    'B X' : 'B X',
    'B Y' : 'B Y',
    'B Z' : 'B Z',
    'C X' : 'C Y',
    'C Y' : 'C Z',
    'C Z' : 'C X'
}


score=0
windrawloselist=[]
for line in f.readlines():
      windrawloselist.append(windrawlosetranslate[line.rstrip('\n')])

print(windrawloselist)
for line in windrawloselist:
    score +=scores[line.rstrip('\n')]

print(score)