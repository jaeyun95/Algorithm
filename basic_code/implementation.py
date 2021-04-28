

## input
#N = 5
#plans = ["R","R","R","U","D","D"]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ["L","R","U","D"]

def implementation1(N,plans):
    x, y = 1, 1
    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue
        x, y = nx, ny
    return nx, ny

# answer is 3, 4
#print(implementation(N,plans))

## input
#N = 1
def implementation2(N):
    count = 0
    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h)+str(m)+str(s):
                    count += 1
    return count
## answer is 3150
#print(implementation2(1))

## input
#N = 'a1'
#x = int(N[1])
#y = int(ord(N[0])) - int(ord('a')) + 1
dx = [-1,1,-1,1,-2,-2,2,2]
dy = [-2,-2,2,2,-1,1,-1,1]
move_types = ["LLU","LLD","RRU","RRD","UUL","UUR","DDL","DDR"]

def implementation3(x,y):
    count = 0
    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            continue
        count += 1
    return count
## answer is 2
#print(implementation3(x,y))

## input
#input_str = "K1KA5CB7"

def implementation4(input_str):
    number = 0
    alpha = []
    for char in input_str:
        if char.isdigit():
            number += int(char)
        else:
            alpha.append(char)
    alpha.sort()
    return "".join(alpha)+str(number) if number > 0 else ""

## answer is ABCKK13
#print(implementation4(input_str))