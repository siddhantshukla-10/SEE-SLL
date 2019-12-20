li = input("Enter space separated integers").split()
arr = [int(i) for i in li]
print("Maximum",max(arr))
print("Minimum",min(arr))
inp = int(input("Enter a number to be inserted"))
arr.append(inp)
print(arr)
inp = int(input("Enter a number to be deleted"))
arr.remove(inp)
print(arr)
inp=int(input("Enter a number to be searched"))
if inp in arr:
	print("Present")
else:
	print("Not Present")

