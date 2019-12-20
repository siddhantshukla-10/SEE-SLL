import sys
import os
from functools import reduce

wordLen = []
dict = {}

if(len(sys.argv)!=2):
	print("Invalid arguments!")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print("File Path does not exist!!")
	sys.exit()

if(sys.argv[1].split('.')[-1]!="txt"):
	print("Invalid file format!!")
	sys.exit()

f = open(sys.argv[1],"r")
for line in f:
	for word in line.split():
		dict[word] = dict.get(word,0) + 1

#print(dict)

sortedDict = sorted(dict.items(), key=lambda x:x[1] ,reverse = True)

for i in range(10):
	try:
		wordTuple = sortedDict[i]
		wordLen.append(len(wordTuple[0]))
		print(wordTuple[0]," FREQUENCY--> ",wordTuple[1])
	except IndexError:
		print("File has less than 10 words!!")
		break

print ("Lengths of 10 most frequently occuring words:")
print (wordLen)

sum1 = reduce(lambda x,y:x+y,wordLen)
print(sum1/10)

square = [x**2 for x in wordLen if x%2 != 0]
print(square)


