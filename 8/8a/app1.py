def AtomiDict():
	dict={"Na":"Sodium","Li":"Lithium","H":"Hydrogen"}
	print("Enter a unique element")
	symbol = input("Enter the symbol")
	value = input("Enter the value")
	dict[symbol]=value
	print(dict)
	print("Enter a duplicate element")
	symbol = input("Enter the symbol")
	value = input("Enter the value")
	dict[symbol]=value
	print(dict)
	print(len(dict))
	symbol = input("Enter the element you want to search!")
	if symbol in dict:
		print("Present and value = ",dict[symbol])
	else:
		print("Not present")

AtomiDict()


