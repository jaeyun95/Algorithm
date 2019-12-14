#(7) day07 이진탐색


def binary_search(numbers, target):
    numbers.sort()
    start = 0
    end = len(numbers)-1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            return mid
        elif  numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False
	
#재귀를 사용한 경우
def binary_search_recursive(numbers, target, start, end):
    if start > end:
        return False

    mid = (start + end)//2

    if numbers[mid] == target:
        return mid
    elif  numbers[mid] < target:
        start = mid + 1
    else:
         end = mid - 1
    return binary_search_recursive(numbers, target, start, end)
