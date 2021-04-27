## greedy search 

## first
coin_list = [500, 100, 50, 10]

def greedy1(num):
    count = 0
    for coin in coin_list:
        count += (num//coin)
        num %= coin
    return count
## answer is 6
#print(greedy(1260))

## second
N, K = 25, 5

def greedy2(N, K):
    count = 0
    while N > 1:
        if N%K != 0:
            N -= 1
        else:
            N //= K
        count += 1
    return count
## answer is 2
#print(greedy2(N,K))
#input_str = "02984" #answer is 576
#input_str = "567" #answer is 210

def greedy3(input_str):
    result = 0
    input_list = list(map(int,list(input_str)))
    for value in input_list:
        if value <=1 or result <= 1: result += 1
        else: result *= value
    return result
#print(greedy3(input_str))
N = 5
X = [2, 3, 1, 2, 2] # answer is 2
def greedy4(X):
    X.sort()
    count, result = 0, 0
    for x in X:
        count += 1
        if x == count:
            result += 1
            count = 0
    return result
print(greedy4(X))
