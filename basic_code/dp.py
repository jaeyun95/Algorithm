
# top-down
cache = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if cache[x] != 0:
        return cache[x]
    cache[x] = fibo(x-1) + fibo(x-2)
    return cache[x]
## input
#N = 4
## output answer is 3
#print(fibo(N))

##bottom-up
cache = [0] * 100
cache[1] = 1
cache[2] = 1
## input
n = 3
for i in range(3, n+1):
    cache[i] = cache[i-1] + cache[i-2]
## output answer is 3
#print(cache[n])


## bottom-up
# input
N = 4
storage = [1,3,1,5]

cache = [0] * N
cache[0] = storage[0]
cache[1] = max(storage[0],storage[1])
for i in range(2,len(storage)):
    if cache[i-2] + storage[i] > cache[i-1]:
        cache[i] = cache[i-2] + storage[i]

## answer is 8
#print(cache[N-1])

## input
X = 26
cache = [0] * (X+1)

for i in range(2,X+1):
    cache[i] = cache[i-1] + 1
    if i % 2 == 0:
        cache[i] = min(cache[i], cache[i//2]+1)
    if i % 3 == 0:
        cache[i] = min(cache[i], cache[i//3]+1)
    if i % 5 == 0:
        cache[i] = min(cache[i], cache[i//5]+1)
## answer is 3
#print(cache[X])

## input
N, M = 2, 15
N_list = [2,3]
cache = [float("INF")] * (M+1)
cache[0] = 0

for n in N_list:
    for m in range(n, M+1):
        if cache[m-n] != float("INF"):
            cache[m] = min(cache[m], cache[m-n]+1)

## answer is 5
#if cache[m] == float("INF"): print(-1)
#else: print(cache[m])

N, M = 3, 4
map = [[1,3,3,2],[2,1,4,1],[0,6,4,7]]
cache = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    cache[n][0] = map[n][0]

for m in range(1,M):
    for n in range(N):
        if n == 0: left_up = 0
        else: left_up = cache[n-1][m-1]
        if n == N-1: left_down = 0
        else: left_down = cache[n+1][m-1]
        left = cache[n][m-1]
        cache[n][m] = map[n][m] + max(left,left_up,left_down)
result = 0
for n in range(N):
    result = max(result,cache[n][M-1])
## answer is 19
#print(result)


