
def radix_sort(lst, base=10):
    def counting_sort(lst, digit, base):
    	size = len(lst)
    	output = [0]*size
    	count = [0]*base
    	for i in range(size):
    		index = int(lst[i]/digit)
    		count[index%base] += 1
    	for i in range(1,base): count[i]+=count[i-1]
    	for i in range(size-1,-1,-1):
    		index = int(lst[i]/digit)
    		output[count[index%base]-1] = lst[i]
    		count[index%base] -= 1
    	for i in range(size): lst[i]=output[i]
    maxval = max(lst)
    digit = 1
    while digit <= maxval:
        counting_sort(lst, digit, base)
        digit *= base
