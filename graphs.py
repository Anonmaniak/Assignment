print("Topic: Implement depth-first search (DFS) for an undirected graph.")

from typing import Dict, List

def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    result = []

    def helper(v):
        if v not in visited:
            visited.add(v)
            result.append(v)
            for neighbor in graph[v]:
                helper(neighbor)

    helper(start)
    return result

graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
start_node = 2
print("DFS starting from 2:", dfs(graph, start_node)) 
