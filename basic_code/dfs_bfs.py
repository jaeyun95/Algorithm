

## input
#N, M = 4, 5
#matrix = [[0,0,1,1,0],
#          [0,0,0,1,1],
#          [1,1,1,1,1],
#          [0,0,0,0,0]]
'''
def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1
'''
## answer is 3
#print(count)

from collections import deque

N, M = 5, 6
maze = [[1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]]

moves = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

    return maze[N-1][M-1]

print(bfs(0,0))