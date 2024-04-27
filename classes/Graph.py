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

    def reset(self) -> None:
        self.dist = [float('inf')] * 10000
        self.pre = [-1] * 10000
        self.routeRef = [tuple()] * 10000
        self.pathRef = [list()] * 10000

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
