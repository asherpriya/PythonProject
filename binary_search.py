import random
import ins_sort

def bin_search(x, ip_arr, lower, upper):	
		#print lower, upper, x
		l = upper-lower+1
		if l==1:
			return ('Element found in position', lower) if x==ip_arr[lower] else 'Not found'
		ptr = lower+(l/2)
		if x == ip_arr[ptr]:
			return 'Element found in position', ptr
		elif x < ip_arr[ptr]:
			return bin_search(x,ip_arr,lower, ptr-1) 
		else:
			return bin_search(x, ip_arr, ptr+1, upper)
					

x=random.randint(0,20)
size=random.randint(3,35)
arr2=[]
for i in range(size):
	arr2.append(random.randint(0,20))

arr2 = ins_sort.ins_sort(arr2)
print 'Array is', arr2
print 'Number to search is ', x
print bin_search(x, arr2, 0, len(arr2)-1)


	
