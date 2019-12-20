import sys
import os
from functools import reduce

if(len(sys.argv)!=2):
	print("Invalid arguments!")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print("File path does not exist!!")
	sys.exit()

if(sys.argv[1].split('.')[-1]!="txt"):
	print("Invalid file format")
	sys.exit()

wordLen = []
dict={}

f = open(sys.argv[1],"r")
for line in f:
	for word in line.split():
		dict[word] = dict.get(word,0) + 1

sortedDict = sorted(dict.items(), key=lambda x:x[1], reverse= True)

for i in range(10):
	wordTuple = sortedDict[i]
	wordLen.append(len(wordTuple[0]))
	print(wordTuple[0], " FREQUENCY--> ",wordTuple[1])

print(wordLen)

sum = reduce(lambda x,y:x+y, wordLen)
print(sum/10)

square = [x**2 for x in wordLen if x%2 != 0]
print(square)

