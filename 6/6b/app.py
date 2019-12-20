class SentenceReverser:
	vowels = ['a','e','i','o','u']
	sentence = ""
	reverse = ""
	vowelCount = 0
	def __init__(self,sentence):
		self.sentence = sentence
		self.reverseSentence()
	def reverseSentence(self):
		self.reverse = " ".join(reversed(self.sentence.split()))
		print(self.reverse)
	def getVowelCount(self):
		vowelCount = sum(s in self.vowels for s in self.sentence.lower())
		return vowelCount
	def getReverseSentence(self):
		return self.reverse

items = []

for i in range(3):
	inp = input("Enter a sentence")
	reverser = SentenceReverser(inp)
	items.append(reverser)

print(items)

sortedItems = sorted(items,key=lambda x:x.getVowelCount(), reverse=True)

for i in range(len(sortedItems)):
	print("Reverse : ",sortedItems[i].getReverseSentence(), " Vowel count: ",sortedItems[i].getVowelCount())
