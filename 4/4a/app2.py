class Rectangle:
	def __init__(self,length=10,breadth=5):
		self.length = length
		self.breadth = breadth
		self.area = self.length * self.breadth
	def accept(self):
		i = int(input("Enter length"))
		self.length = i
		b = int(input("Enter breadth"))
		self.breadth = b
		self.area = self.length * self.breadth
	def display(self):
		print("Length ",self.length)
		print("Breadth ",self.breadth)
		print("Area ",self.area)


st = Rectangle()
while(1):
	i = int(input("1-Display\n2-Modify\n3-Exit"))
	if(i==1):
		st.display()
	elif(i==2):
		st.accept()
	elif(i==3):
		exit()
	else:
		print("Invalid choice!")


