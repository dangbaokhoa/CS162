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
    
    def addEdge(self, startStop, nextStop, weight) -> None:
        self.adj[startStop].append((nextStop, weight))

    def dijkstra(self, src) -> None:
        pq = []
        heapq.heappush(pq, (0, src))
        self.dist[src] = 0
        while pq:
            shortestU, startStop = heapq.heappop(pq)
            for nextStop, value in self.adj[startStop]:
                routeId, routeVarId = value[2], value[3]
                lngPath, latPath = value[4], value[5]
                distanceBetweenTwopStop = value[0]
                if self.dist[nextStop] > shortestU + distanceBetweenTwopStop:
                    self.dist[nextStop] = shortestU + distanceBetweenTwopStop
                    self.pre[nextStop] = startStop
                    self.top[nextStop] += 1
                    self.routeRef[nextStop] = (routeId, routeVarId)
                    self.pathRef[nextStop] = (lngPath, latPath)
                    heapq.heappush(pq, (self.dist[nextStop], nextStop))
                    
    def floyd(self, allStop) -> None:
        for startVertice in allStop:
            for midVertice in allStop:
                for endVertice in allStop:
                    if (self.distFloyd[startVertice][midVertice] + self.distFloyd[midVertice][endVertice] < self.distFloyd[startVertice][endVertice]):
                        self.distFloyd[startVertice][endVertice] = self.distFloyd[startVertice][midVertice] + self.distFloyd[midVertice][endVertice]
                        
    def dfsIn(self, startStop, flag): 
        if self.dp_in[startStop] != 0:
            return self.dp_in[startStop]
        result = 0
        for nextStop in self.in_dag[startStop]:
            result = result + self.dfsIn(nextStop, 1)
        if result == 0:
            result = flag
        self.dp_in[startStop] = result
        return result
    
    def dfsOut(self, startStop, flag): 
        if self.dp_out[startStop] != 0:
            return self.dp_out[startStop]
        result = 0
        for nextStop in self.in_dag[startStop]:
            result = result + self.dfsOut(nextStop, 1)
        if result == 0:
            result = flag
        self.dp_out[startStop] = result
        return result
    
    def buildGraph(self, startStop) -> None:
        for nextStop, w in self.adj[startStop]:
            if self.dist[nextStop] == self.dist[startStop] + w[0]:
                self.in_dag[startStop].append(nextStop)
                self.out_dag[nextStop].append(startStop)
                
    def calculateImportantStop(self, startStop, allStop) -> None:
        self.buildGraph(startStop)
        for vertice in allStop:
            self.dfsIn(vertice, 0)
            self.dfsOut(vertice, 0)
        for vertice in allStop:
            self.top[vertice] += self.dp_in[vertice] * self.dp_out[vertice]
                
class GraphQuery:
    def __init__(self) -> None:
        pass
        
    def outputAsJSON(self, OUTPUT_FILENAME, result):
        OUTPUT_FILE_PATH = os.path.abspath("output/{}")
        os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
        with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
            text = json.dumps(result, default=lambda o: o.__dict__, ensure_ascii=False)
            f.write(text + "\n")
  
    def outputAllPairDistance(self, OUTPUT_FILENAME, result) -> None:
        OUTPUT_FILE_PATH = os.path.abspath("output/{}")
        os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
        with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
            COLUMN_NAME = ["StartStopId", "EndStopId", "Time"]
            f.write(",".join(COLUMN_NAME) + "\n")
            for i in result:
                text = "{},{},{}".format(i["Start"], i["End"], i["Time"])
                f.write(text + "\n")
