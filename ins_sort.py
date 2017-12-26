import random

def ins_sort(ip_arr):
   l=len(ip_arr)
   for j in range(1,l):
     nxt=ip_arr[j]
     i=j-1
     while(i>=0 and ip_arr[i]>nxt):
            ip_arr[i+1]=ip_arr[i]
            i-=1
     ip_arr[i+1]=nxt
   return ip_arr

if __name__=='__main__':
	l = random.randint(5, 100)
	arr = []
	for i in range(l):
		arr.append(random.randint(0, 100))

	print 'Original Array', arr
	arr = ins_sort(arr)
	print 'Sorted Array', arr
