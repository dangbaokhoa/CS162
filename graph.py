from classes.Graph import *
from stops import getListStop
from vars import getListRoute
from paths import getListPath
from utils.converter import *
from math import sqrt, pow

def almost_equal(a, b, tolerance=1e-5):
    return abs(a - b) <= tolerance

def findDistance(path, lngPath, latPath, fData, sData):
  flag = False
  distance = 0.0
  for j in range(len(path.lng)):
    if flag:
      XI, YI = lnglatToXY(path.lng[j - 1], path.lat[j - 1])
      XJ, YJ = lnglatToXY(path.lng[j], path.lat[j])           
      if not (XI == None or YI == None or XJ == None or YJ == None): distance += sqrt(pow(XI - XJ, 2) + pow(YI - YJ, 2))

    if almost_equal(path.lng[j], fData["Lng"]) and almost_equal(path.lat[j], fData["Lat"]): 
      flag = 1

    if flag:
      lngPath.append(path.lng[j])
      latPath.append(path.lat[j])
      
    if almost_equal(path.lng[j], sData["Lng"]) and almost_equal(path.lat[j], sData["Lat"]):
      break

  return distance

def buildGraph():
  global allStop
  global allCoor
  allStop = list()
  allCoor = list()

  for res in listStop.stopGroup:
    # Get routeId and routeVarId of stop
    routeId = int(res.RouteId)
    routeVarId = int(res.RouteVarId)
    runningTime = None
    totalDistance = None
    # Get running time and total distance of route
    for routes in listRoute.routeGroup:
      for route in routes.routeVar:
        if (route["RouteId"] == routeId):
          runningTime = route["RunningTime"]
          totalDistance = route["Distance"]
          break
  
    if not runningTime or not totalDistance:
      continue
    # Get path have same RouteId and RouteVarId
    choosenPath = None
    for paths in listPath.pathGroup:
      if int(paths.RouteId) == routeId and int(paths.RouteVarId) == routeVarId:
        choosenPath = paths
    if not choosenPath:
      continue
    
    # Store all stopId and coordinate of stop
    for stop in res.Stops: 
      allStop.append(stop["StopId"])
      allCoor.append((stop["Lng"], stop["Lat"]))

    # Calculate average running time between 2 stops
    runningTime = (runningTime * 60)
    timeBase = runningTime / totalDistance
    # Calculate average distance between 2 stops
    for i in range(len(res.Stops) - 1):
      lngPath = list()
      latPath = list()

      distance = findDistance(choosenPath, lngPath, latPath, res.Stops[i], res.Stops[i + 1]) 
      timeCost = distance * timeBase
      
      # Add edge between 2 stops
      g.addEdge(res.Stops[i]["StopId"], res.Stops[i + 1]["StopId"], (timeCost, distance, routeId, routeVarId, lngPath, latPath))
  
  allStop = list(set(allStop))   
  
def allPairDistance(): 
  res = list()
  for i in range(len(allStop)):
    g.dijkstra(allStop[i])
    g.calculateImportantStop(allStop[i], allStop)
    for j in range(len(allStop)):
      if i == j:
        continue
      res.append({
        "Start": allStop[i],
        "End": allStop[j],
        "Time": abs(g.dist[allStop[j]])
      })
    g.reset()
  OUTPUT_FILENAME_JSON = "all_pair_distance.json"
  GraphQuery().outputAllPairDistance(OUTPUT_FILENAME_JSON, res)

def mostImportantPath():
  res = list()
  sortedAllStop = sorted(allStop, key = lambda x: g.top[x], reverse=True)
  for i in range(10):
    flag = 0
    for _stop in listStop.stopGroup:
      if flag: break
      for stop in _stop.Stops:
        if flag: break
        if sortedAllStop[i] == stop["StopId"]:
          flag = 1
          res.append(stop)

  OUTPUT_FILENAME_JSON = "top_10_important_path.json"
  GraphQuery().outputAsJSON(OUTPUT_FILENAME_JSON, res)

def shortestPath(u, v):
  if u == None or v == None: return
  g.reset()
  g.dijkstra(u)
  res = dict()
  res["StartStopId"] = u
  res["EndStopId"] = v
  res["RunningTime"] = g.dist[v]

  stopIds = list()
  while (v != -1 and u != v):
    stopIds.append(v)
    v = g.pre[v]
    if (u == v):
      stopIds.append(v)
      break
  stopIds.reverse()
  
  res["StopIds"] = stopIds

  pathRoute = list()
  for stopId in stopIds:
    if g.routeRef[stopId]: 
      pathRoute.append({ "lat": g.pathRef[stopId][1], "lng": g.pathRef[stopId][0], "RouteId": g.routeRef[stopId][0], "RouteVarId": g.routeRef[stopId][1]})    

  res["Path"] = pathRoute
  
  OUTPUT_FILENAME_JSON = "shortest_path.json"
  GraphQuery().outputAsJSON(OUTPUT_FILENAME_JSON, res)

if __name__ == "__main__":
  g = Graph()

  listRoute = getListRoute()
  listStop = getListStop()
  listPath = getListPath()
  
  # 1. Build graph
  buildGraph()

  ### WARNING: This function will take a long time to run
  # 2. Print shortest path from all pair in graph
  allPairDistance()

  # 4. Print 10 most important path
  mostImportantPath()

  # 3. Print shortest path from startStop to endStop

  startStop = input("Enter start stop: ")
  endStop = input("Enter end stop: ")
  startStop = int(startStop)
  endStop = int(endStop)
  shortestPath(startStop, endStop)
