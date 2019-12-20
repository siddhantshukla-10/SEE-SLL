class Student:
	def __init__(self):
		self.name = ""
		self.age = 0
		self.marks = []
	def accept(self):
		inp = input("Enter name")
		self.name = inp
		inp = int(input("Enter age"))
		self.age = inp
		for i in range(3):
			inp = int(input("enter marks"))
			self.marks.append(inp)
	def display(self):
		print(self.name)
		print(self.age)
		print(self.marks)

siddhant = Student()
siddhant.accept()
siddhant.display()
