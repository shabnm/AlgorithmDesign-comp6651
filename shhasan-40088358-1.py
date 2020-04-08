from collections import defaultdict
import collections
import heapq

class Graph():
    def __init__(self):
        #{'X': [9, 'A'],'A':[9, 'X'], ...} adjacency list
        self.edges = defaultdict(list)
    
    def add_edge(self, node1, node2, weight):
        self.edges[node1].append([weight, node2])
        self.edges[node2].append([weight, node1])

def shortestPath(graph, source, des='z'):
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == des:
                return (cost, path)
            for c, neighbour in graph.edges[node]:
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+c, neighbour, path))

src = set() 
n = int(input()) 
graph = Graph() 
for i in range(0, n):
  ele = input().split(" ")
  if ele[0].isupper():
    src.add(ele[0])
  if ele[1].isupper():
    src.add(ele[1])
  ele[2] = int(ele[2])
  graph.add_edge(*ele)

cost = float('inf')
for s in src:
  path = shortestPath(graph, s)
  if path[0] < cost:
    cost = path[0]
    meadow = path[1][0]
  
s = meadow  +" "+  str(cost)
print(s)