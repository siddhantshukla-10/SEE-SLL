print("List of space separated integers")
li = input().split()
arr = [int(a) for a in li]
print("Maximum ",max(arr))
print("Minimum ",min(arr))
print("Enter an element to be inserted!")
inp = int(input())
arr.append(inp)
print(arr)
print("Enter an element to be deleted!")
inp = int(input())
arr.remove(inp)
print(arr)
print("Enter an element to be searched!")
inp = int(input())
if inp in arr:
	print("Present")
else:
	print("Not Present")
