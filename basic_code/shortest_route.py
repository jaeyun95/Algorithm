
## floyd warshall
V, E = 5, 6
E_list = [[5,1,1],[1,2,2],[1,3,3],[2,3,4],[2,4,5],[3,4,6]]
graph = [[float("INF") for _ in range(V+1)] for _ in range(V+1)]

for i in range(1,V+1):
    for j in range(1,V+1):
        if i==j: graph[i][j] = 0

for s, e, w in E_list:
    graph[s][e] = w

for k in range(1,1+V):
    for a in range(1,1+V):
        for b in range(1,1+V):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

#for a in range(1,1+V):
#    for b in range(1,1+V):
#        print(a,"-->",b," = ",graph[a][b])

## input
import heapq

V, E, start = 3, 2, 1
E_list = [[],[[2,4],[3,2]],[],[]]
graph = {node:float("INF") for node in range(1,V+1)}
heap = []
graph[start] = 0
heapq.heappush(heap,[graph[start],start])
while heap:
    dis, node = heapq.heappop(heap)
    for e, num in E_list[node]:
        if graph[e] > (dis + num):
            graph[e] = dis+num
            heapq.heappush(heap,[(dis+num),node])
count = 0
hour = 0
for k, v in graph.items():
    if k == start: continue
    if v != float("INF"):
        count += 1
        hour = max(hour,v)
## output is 2 4
#print(count,hour)

# input
V, E = 5, 7
E_list = [[1,4],[1,2],[1,3],[2,4],[3,4],[3,5],[4,5]]
X, K = 4, 5
graph = [[float("INF") for _ in range(V+1)] for _ in range(V+1)]
for i in range(1,V+1):
    for j in range(1,V+1):
        if i==j: graph[i][j] = 0

for s,e in E_list:
    graph[s][e] = 1
    graph[e][s] = 1

for i in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

distance = graph[1][K] + graph[K][X]
if distance > float("INF"): print("-1")
else: print(distance)




