#(5) day05 삽입정렬

def insert_sort(numbers):
    for i in range(1,len(numbers)):
       for j in range(i, 0, -1):
			if numbers[j] < numbers[j-1]:
				numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
			else: break
    return numbers
	

