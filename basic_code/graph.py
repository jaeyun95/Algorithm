
v = [1,2,3,4,5,6,7]
e = [[1,2,29],[1,5,75],[2,3,35],[2,6,34],[3,4,7],[4,6,23],[4,7,13],[5,6,53],[6,7,25]]
parent = [0] * (len(v)+1)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b: parent[b] = a
    else: parent[a] = b

for i in range(1,len(v)+1):
    parent[i] = i

#for i in range(len(e)):
#    a, b = e[i][0], e[i][1]
#    union_parent(parent, a, b)
#print(parent)

###krustkal
v = [1,2,3,4,5,6,7]
edges = [[1,2,29],[1,5,75],[2,3,35],[2,6,34],[3,4,7],[4,6,23],[4,7,13],[5,6,53],[6,7,25]]
result = 0

edges.sort(key=lambda x:x[2])
for edge in edges:
    a, b, cost = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

## output is 159
#print(result)

## topology sort
from collections import deque
v, e = 7, 8
indegree = [0] *(v+1)
input_ = [[1,2],[1,5],[2,3],[2,6],[3,4],[4,7],[5,6],[6,4]]
graph = [[] for i in range(v+1)]

for a, b in input_:
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")
#topology_sort()




