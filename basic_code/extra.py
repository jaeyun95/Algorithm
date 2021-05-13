import math

def is_prime_number(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def is_prime_number2(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

n = 26
array = [True for i in range(n+1)]
def is_prime_number3(x):
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
## False
#print(is_prime_number(4))
## True
#print(is_prime_number(5))
# answer is 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#for i in range(2,n+1):
#    if array[i]:
#        print(i, end=" ")

x = 5
n = 5
data = [1,2,3,2,5]
def two_pointer(x,n):
    count, end, interval_sum = 0, 0, 0
    for start in range(n):
        while interval_sum < x and end < n:
            interval_sum += data[end]
            end += 1
        if interval_sum == x:
            count += 1
        interval_sum -= data[start]
    return count
# answer is 3
#print(two_pointer(x,n))
input_list = [10,20,30,40,50]
prefix_sum = [0 for _ in range(len(input_list)+1)]
left, right = 3, 4
for i in range(1,len(input_list)+1):
    prefix_sum[i] = prefix_sum[i-1] + input_list[i-1]
## answer 70
print(prefix_sum[right]-prefix_sum[left-1])