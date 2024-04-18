import heapq
from collections import defaultdict 
import os
import json

class Graph: 
    def __init__(self):
        # Dijkstra
        self.adj = defaultdict(list)
        self.dist = [float('inf')] * 10000
        
        self.top = [0] * 10000
        self.pre = [-1] * 10000
        self.routeRef = [tuple()] * 10000
        self.pathRef = [list()] * 10000
        
        self.in_dag = defaultdict(list)
        self.out_dag = defaultdict(list)
        self.dp_in = [0] * 10000
        self.dp_out = [0] * 10000

        # Floyd
        self.distFloyd = [[float('inf')] * 10000 for _ in range(10000)]
        
    def reset(self) -> None:
        self.dist = [float('inf')] * 10000
        self.pre = [-1] * 10000
        self.routeRef = [tuple()] * 10000
        self.pathRef = [list()] * 10000
        
        self.in_dag = defaultdict(list)
        self.out_dag = defaultdict(list)
        self.dp_in = [0] * 10000
        self.dp_out = [0] * 10000
    
    def addEdge(self, u, v, w) -> None:
        self.adj[u].append((v, w))

    def dijkstra(self, src) -> None:
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
                    
    def floyd(self, allStop) -> None:
        for startVertice in allStop:
            for midVertice in allStop:
                for endVertice in allStop:
                    if (self.distFloyd[startVertice][midVertice] + self.distFloyd[midVertice][endVertice] < self.distFloyd[startVertice][endVertice]):
                        self.distFloyd[startVertice][endVertice] = self.distFloyd[startVertice][midVertice] + self.distFloyd[midVertice][endVertice]
                        
    def dfsIn(self, u, flag): 
        if self.dp_in[u] != 0:
            return self.dp_in[u]
        res = 0
        for v in self.in_dag[u]:
            res = res + self.dfsIn(v, 1)
        if res == 0:
            res = flag
        self.dp_in[u] = res
        return res
    def dfsOut(self, u, flag): 
        if self.dp_out[u] != 0:
            return self.dp_out[u]
        res = 0
        for v in self.in_dag[u]:
            res = res + self.dfsOut(v, 1)
        if res == 0:
            res = flag
        self.dp_out[u] = res
        return res
    def buildGraph(self, u) -> None:
        for v, w in self.adj[u]:
            if self.dist[v] == self.dist[u] + w[0]:
                self.in_dag[u].append(v)
                self.out_dag[v].append(u)
    def calculateImportantStop(self, u, allStop) -> None:
        self.buildGraph(u)
        for vertice in allStop:
            self.dfsIn(vertice, 0)
            self.dfsOut(vertice, 0)
        for vertice in allStop:
            self.top[vertice] += self.dp_in[vertice] * self.dp_out[vertice]
                
class GraphQuery:
    def __init__(self) -> None:
        pass
        
    def outputAsJSON(self, OUTPUT_FILENAME, res):
        OUTPUT_FILE_PATH = os.path.abspath("output/{}")
        os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
        with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
            text = json.dumps(res, default=lambda o: o.__dict__, ensure_ascii=False)
            f.write(text + "\n")
  
    def outputAllPairDistance(self, OUTPUT_FILENAME, res) -> None:
        OUTPUT_FILE_PATH = os.path.abspath("output/{}")
        os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
        with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
            COLUMN_NAME = ["StartStopId", "EndStopId", "Time"]
            f.write(",".join(COLUMN_NAME) + "\n")
            for i in res:
                text = "{},{},{}".format(i["Start"], i["End"], i["Time"])
                f.write(text + "\n")
