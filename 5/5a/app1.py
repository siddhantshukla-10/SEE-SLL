TempData = []
def celToFar():
	inp = float(input("Enter temperature in centigrade"))
	far = ((inp-32)*5)/9
	data = (inp,far)
	TempData.append(data)
	print(TempData)

def farToCel():
	inp = float(input("Enter temperature in fahrenheit"))
	cel = ((inp*9)/5)+32
	data = (cel,inp)
	TempData.append(data)
	print(TempData)


while(True):
	inp = int(input("1-Cel to Far\n2-Far to Cel\n3-Exit"))
	if(inp==1):
		celToFar()
	elif(inp==2):
		farToCel()
	elif(inp==3):
		exit()
	else:
		print("Invalid choice")
