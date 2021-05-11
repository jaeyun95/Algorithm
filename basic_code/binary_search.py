
from bisect import bisect_left, bisect_right
'''
example = [1,2,4,4,8]
x = 4
print(bisect_left(example,x))
print(bisect_right(example,x))
'''
'''
example = [1,2,3,3,3,3,4,4,5,8]
x = 3
left = bisect_left(example,3)
right = bisect_right(example,3)
print(right-left)
'''

# input
N, M = 4, 6
height = [19,15,10,17]

start, end = 0, max(height)
result = 0
while start <= end:
    mid = (start + end)//2
    total = 0
    for h in height:
        if h - mid > 0:
            total += (h-mid)
    if total >= M:
        result = mid
        start = mid + 1
    else: end = mid -1

## output is 15
#print(result)

input = [1,1,2,2,2,2,3]
x = 2
if x not in input: print(-1)
else:
    left = bisect_left(input,x)
    right = bisect_right(input,x)
    print(right-left)

