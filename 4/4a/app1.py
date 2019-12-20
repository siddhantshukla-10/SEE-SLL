class Rectangle:
	def __init__(self,length=10,breadth=5):
		self.length = length
		self.breadth = breadth
		self.area = self.length * self.breadth

	def accept(self):
		inp = int(input("Enter length"))
		self.length = inp
		inp = int(input("Enter breadth"))
		self.breadth = inp
		self.area = self.length * self.breadth
	
	def display(self):
		print("Length ",self.length)
		print("Breadth ",self.breadth)
		print("Area ",self.area)


st = Rectangle()
while(True):
	print("1-Display\n2-Modify\n3-Exit!")
	n=int(input())
	if(n==1):
		st.display()
	elif(n==2):
		st.accept()
	elif(n==3):
		exit()
	else:
		print("Invalid choice")


