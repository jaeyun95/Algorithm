
test_graph = {1: set([2,3]),
              2: set([4,5,6]),
              3: set([7]),
              4: set([1]),
              5: set([2,5]),
              6: set([8]),
              7: set([3]),
              8: set([2,3])
              }

def dfs_iteration(graph, root):
    visited = []
    stack = [root]
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(graph[now])
    return visited

def dfs_recursive(graph, start, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited
