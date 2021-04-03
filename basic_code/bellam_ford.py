test_graph = {
    '0': {'1': 6, '2':  7},
    '1': {'2':  8, '3':  5, '4': -4},
    '2': {'3': -3, '4': 9},
    '3': {'1': -2},
    '4': {'0': 8, '3':7}
}

def bellman_ford(graph, start):
    distance, predecessor = {node:float('INF') for node in graph}, {node:None for node in graph}
    distance[start] = 0
    for _ in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor], predecessor[neighbor] = distance[node] + graph[node][neighbor], node

    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1
    return distance
