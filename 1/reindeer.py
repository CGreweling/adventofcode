#!/bin/python
import collections


f = open("reindeer_data.txt", "r")

reindeer={}
reindeers=collections.namedtuple('name', 'loads')
i=1
load=0
for line in f.readlines():
    if len(line.rstrip('\n')) != 0:
      load+=int(line.rstrip('\n'))
    elif len(line.rstrip('\n')) == 0:
      print(str(i) +  "load"+ str(load))
      reindeer[i]=load
      i+=1
      load=0
sortedreindeer = sorted(reindeer.items(), key=lambda x: x[1])
print(sortedreindeer)