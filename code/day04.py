#(4) day04 버블정렬

def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers
	

