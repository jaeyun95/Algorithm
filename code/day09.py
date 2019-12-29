#(9) day09 이진수 십진수 변환

def demical_to_binary(number):
    answer = 0
    multiple = 1
    while number > 0:
        answer += number%2 * multiple
        multiple *= 10
        number = number // 2
    return answer
	
def binary_to_demical(number):
    answer = 0
    multiple = 1
    while number > 0:
        answer += number%10 * multiple
        multiple *= 2
        number = number // 10
    return answer
	

