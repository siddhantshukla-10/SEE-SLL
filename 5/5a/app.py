TempData=[]
def celToFar():
	temp=float(input("Enter number in celsius"))	
	far=((temp-32)*5)/9
	data = (temp,far)
	TempData.append(data)
	print("From far to cel is ",data)

def farToCel():
	temp=float(input("Enter number in farenheit"))	
	cel=((temp*9)/5)+32
	data = (temp,cel)
	TempData.append(data)
	print("From cel to far is ",data)

while(1):
	choice = int(input("1 for cel to far \n 2 for far to cel \n 3 for display \n 4 for exit"))
	if (choice==1):
		celToFar()
	elif (choice==2):
		farToCel()
	elif (choice==3):
		print(TempData)
	elif (choice==4):
		exit(0)




