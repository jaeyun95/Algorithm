import heapq

test_graph = {'0': {"1":10,"2":5},
              '1': {"2":2,"3":1},
              '2': {"1":3,"3":9,"4":2},
              '3': {"4":4},
              '4': {"0":7,"3":6}
              }

def dijkstra(graph, start):
    distance = {node : float('inf') for node in graph}
    distance[start] = 0
    heap = []
    heapq.heappush(heap,[distance[start],start])
    while heap:
        current_dist, current_node = heapq.heappop(heap)

        for next_node, dis in graph[current_node].items():
            if distance[next_node] > (dis + current_dist):
                distance[next_node] = dis + current_dist
                heapq.heappush(heap, [(dis + current_dist), next_node])
    return distance
