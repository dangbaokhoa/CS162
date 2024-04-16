import heapq
from collections import defaultdict 
import os
import json

class Graph: 

  def __init__(self):
    self.adj = defaultdict(list)
    self.dist = [float('inf')] * 10000
    self.top = [1] * 10000
    self.pre = [-1] * 10000
    self.routeRef = [tuple()] * 10000
    self.pathRef = [list()] * 10000

  def reset(self):
    self.dist = [float('inf')] * 10000
    self.pre = [-1] * 10000
    self.routeRef = [tuple()] * 10000
    self.pathRef = [list()] * 10000
  
  def addEdge(self, u, v, w):
    self.adj[u].append((v, w))

  def dijkstra(self, src):
    pq = []
    heapq.heappush(pq, (0, src))
    self.dist[src] = 0
    while pq:
      du, u = heapq.heappop(pq)
      for v, w in self.adj[u]:
        r = (w[2], w[3])
        uv = w[0]
        if self.dist[v] > du + uv:
          self.dist[v] = du + uv
          self.pre[v] = u
          self.top[v] += 1
          self.routeRef[v] = r
          self.pathRef[v] = (w[4], w[5])
          heapq.heappush(pq, (self.dist[v], v))

class GraphQuery:
  def __init__(self) -> None:
    pass
        
  def outputAsJSON(self, OUTPUT_FILENAME, data):
    OUTPUT_FILE_PATH = os.path.abspath("output/{}")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
    with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
      text = json.dumps(data, default=lambda o: o.__dict__, ensure_ascii=False)
      f.write(text + "\n")
  
  def outputAllPairDistance(self, OUTPUT_FILENAME, data) -> None:
    OUTPUT_FILE_PATH = os.path.abspath("output/{}")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
    with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
      COLUMN_NAME = ["StartStopId", "EndStopId", "Time"]
      f.write(",".join(COLUMN_NAME) + "\n")
      for i in data:
        text = "{},{},{}".format(i["Start"], i["End"], i["Time"])
        f.write(text + "\n")