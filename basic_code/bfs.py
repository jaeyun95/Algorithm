
test_graph = {1: set([2,3]),
              2: set([4,5,6]),
              3: set([7]),
              4: set([1]),
              5: set([2,5]),
              6: set([8]),
              7: set([3]),
              8: set([2,3])
              }

def bfs_iteration(graph, root):
    visited = []
    queue = [root]
    while queue:
        now = queue.pop(0)
        if now not in visited:
            visited.append(now)
            queue.extend(graph[now])
    return visited