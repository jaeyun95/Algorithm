#(3) day03 퀵정렬

def quick_sort(numbers):
    if len(numbers)<2:
        return numbers
    else:
        pivot = numbers[0]
        pre = [number for number in numbers[1:] if number <= pivot]
        after = [number for number in numbers[1:] if number > pivot]
        return quick_sort(pre) + [pivot] + quick_sort(after)
	

