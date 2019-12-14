#(5) day05 재귀를 사용한 리스트의 합

def recursive(numbers):
    print("===================")
    print('receive : ',numbers)
    if len(numbers)<2:
        print('end!!')
        return numbers.pop()
    else:
        pop_num = numbers.pop()
        print('pop num is : ',pop_num)
        print('rest list is : ',numbers)
        sum = pop_num + recursive(numbers)
        print('sum is : ',sum)
        return sum
	

