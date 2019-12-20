from functools import reduce
a = [1,2,3,4,5,6]
new_a = [i*3 for i in a]
sum1 = reduce(lambda x,y:x+y, a)
sum2 = reduce(lambda x,y:x+y, new_a)
print(sum1)
print(sum2)
