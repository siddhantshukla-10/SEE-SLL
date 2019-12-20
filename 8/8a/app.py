def atomicDictionary():
	dict={'Na':'Sodium','H':'Hydrogen','O':'Oxygen','Li':'Lithium'}
	print("Enter unique element\n")
	symbol=input("Enter the symbol\n")
	name=input("Enter the name\n")
	dict[symbol]=name
	print(dict)
	print("Enter duplicate element\n")
	symbol1=input("Enter the symbol\n")
	name1=input("Enter the name\n")
	dict[symbol1]=name1
	print(dict)
	num=len(dict)
	print("Number of atomic elements in the dictionary are ",num,"\n")
	search=input("Enter the symbol to be searched in the dictionary\n")
	if search in dict:
		print("Present\n")
		print("Value = ",dict[search],"\n")
	else:
		print("Not present\n")      


	
