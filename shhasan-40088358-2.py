from collections import defaultdict
import collections
import itertools

class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
    
    def add_edge(self, node1, node2):
        self.edges[node1].append(node2)
        self.edges[node2].append(node1)

    def check_dominant(self):
      counter = 0
      subsets = []
      for count in range(0,len(self.edges)):
        for j in itertools.combinations(self.edges, count+1):
          subsets.append(j)
        while subsets:
          current_set = subsets[0]
          vertex2 = list(self.edges.keys())
          check1 = list(subsets.pop(0))
          while check1:
            vertex = check1.pop(0)
            try:
                vertex2.remove(vertex)
            except Exception:
                pass
            adjacent = self.edges[vertex]
            for a in adjacent:
              try:
                vertex2.remove(a)
              except Exception:
                pass
            if not check1:
              if not vertex2:
                counter = counter+1
        subsets.clear()
      return counter

edges = defaultdict(list)
n = int(input())
for i in range(0, n):
  ele = input().split(" ")
  ele = list(map(int, ele))
  edges[i] = ele
graph = Graph()
while len(edges) > 1:
    k1 = len(edges)-1
    edge1 = edges.pop(k1)
    for edge in edges:
      k2 = edge
      edge2 = edges[edge]
      max1 = max(edge1[0],edge2[0])
      min1 = min(edge1[1], edge2[1])
      if max1 <= min1:
          graph.add_edge(k1,k2)

edges.clear()
print(graph.check_dominant())
