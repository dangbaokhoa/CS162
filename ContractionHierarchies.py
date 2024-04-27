import heapq
from collections import defaultdict
from typing import List, Tuple  # Add missing import statements

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, source):
        pq: List[Tuple[float, None]] = [(0, source)]  # Fix type annotations
        dist = defaultdict(lambda: float('inf'))
        dist[source] = 0
        prev = {}

        while pq:
            cost, node = heapq.heappop(pq)
            if cost > dist[node]:
                continue
            for neighbor, weight in self.graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    prev[neighbor] = node
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        return dist, prev

    def reconstruct_path(self, prev, target):
        path = []
        while target in prev:
            path.append(target)
            target = prev[target]
        return path[::-1]

def contract(graph, node):
    for u, v, w in graph.edges:
        if u == node:
            for x, y, z in graph.edges:
                if y == node and x != v:
                    new_weight = graph.dist[u] + w + graph.dist[v]
                    if new_weight < graph.dist[x]:
                        graph.dist[x] = new_weight

def contract_hierarchy(graph, source):
    graph.dist, prev = graph.dijkstra(source)
    nodes = list(graph.dist.keys())
    nodes.sort(key=lambda x: graph.dist[x])
    for node in nodes:
        contract(graph, node)
    return prev

# Example usage:
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

prev = contract_hierarchy(g, 0)

# Query shortest path
source = 0
target = 4
shortest_path = g.reconstruct_path(prev, target)
print(f"Shortest path from node {source} to node {target} is: {shortest_path}")
