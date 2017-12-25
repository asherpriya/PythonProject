import random

def lin_search(x, ip_arr):
	l=len(ip_arr)
	for i in range(l):
		if x==ip_arr[i]:
			return i
	return "Element does not exist in array!"

size = random.randint(3, 50)
arr1 = []
for i in range(size):
	arr1.append(random.randint(0, 20))

x = random.randint(0, 20)
print 'Array is', arr1
print 'Number to search is', x
print lin_search(x, arr1)

