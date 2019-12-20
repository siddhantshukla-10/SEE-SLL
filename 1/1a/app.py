print("Enter list of numbers")
a=input().split()
arr = [int(i) for i in a]
print("Maximum: ",max(arr))
print("Minimum: ",min(arr))
print("Enter element to be inserted!")
i=int(input())
arr.append(i)
print("Enter element to be deleted!")
i=int(input())
arr.remove(i)
print("Enter element to be searched!")
i=int(input())
if i in arr:
	print("Present!")
else:
	print("Not Present!")
