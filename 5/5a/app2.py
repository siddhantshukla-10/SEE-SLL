TempData=[]
def celToFar():
	cel = float(input("Enter temperature in centigrade"))
	far = ((cel-32)*5)/9
	data = (cel,far)
	TempData.append(data)
	print(TempData)

def farToCel():
	far = float(input("Enter temperature in farenheit"))
	cel = ((far*9)/5)+32
	data = (cel,far)
	TempData.append(data)
	print(TempData)


while(1):
	i = int(input("1-Cel to Far\n2-Far to Cel\n3- EXIT"))
	if(i==1):
		celToFar()
	elif(i==2):
		farToCel()
	elif(i==3):
		exit()
	else:
		print("Invalid Choice!")


