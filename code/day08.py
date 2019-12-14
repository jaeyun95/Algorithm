#(8) day08 쉘정렬

# gap = (N/2)인 경우
def shell_sort1(numbers):
    number_len = len(numbers)
    gap = (number_len//2)
    while gap > 0:
        if gap%2 == 0: gap += 1
        for i in range(gap,number_len):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap]>temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        gap //=2
    return numbers

# gap = (N/3)+1인 경우
def shell_sort2(numbers):
    number_len = len(numbers)
    gap = (number_len//3)+1
    while True:
        for i in range(gap,number_len):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap]>temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        if gap == 1: return numbers
        gap = (gap//3)+1
	

