class Rectangle:
	def __init__(self,length=10,breadth=5):
		self.length=length
		self.breadth=breadth
		self.area=(self.length)*(self.breadth)
	def accept(self):
		self.length=int(input("Enter the Length"))
		self.breadth=int(input("Enter the breadth"))
	def display(self):
		self.area=self.length*self.breadth
		print("Length = ",self.length)
		print("Breadth = ",self.breadth)
		print("Area = ",self.area)

st=Rectangle()
while(True):
	print("Enter 1-display\n2-modify\n3-exit")
	n=int(input())
	if(n==1):
		st.display()
	elif(n==2):
		st.accept()
	else:
		exit(0)
