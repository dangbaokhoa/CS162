import os
import json
pathKey = ["lng", "lat", "RouteId", "RouteVarId"]
class Path: 
  def __init__(self, path):
    for key, value in path.items():
      setattr(self, key, value)

  def setProperty(self, key, value):
    setattr(self, key, value)

  def getProperty(self, key):
    return getattr(self, key)

class PathQuery():
  def __init__(self, pathGroup):
    self.pathGroup = pathGroup

  def searchByLngLat(self, lng, lat):
    listPath = []
    for paths in self.pathGroup:
      for i in range(len(paths.lat)):
        if paths.lat[i] == lat and paths.lng[i] == lng:
          listPath.append({"lng": paths.lng[i], "lat": paths.lat[i],"RouteId": paths.RouteId, "RouteVarId": paths.RouteVarId})
    return listPath
  
  def outputAsCSV(self, OUTPUT_FILE_PATH, data):
    if not data:
      return
    OUTPUT_FILE_PATH = os.path.abspath("output/paths.csv")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)
    with open(OUTPUT_FILE_PATH, 'w', encoding="UTF-8") as f:
      f.write(",".join(pathKey) + "\n")
      for i in data:
        for route in i.values():
          f.write(str(route) + ",")
        f.write("\n")
        
  def outputAsJSON(self, OUTPUT_FILE_PATH, data):
    OUTPUT_FILE_PATH = os.path.abspath("output/paths.json")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)
    with open(OUTPUT_FILE_PATH, 'w', encoding="UTF-8") as f:
      for i in data:
        i = [i]
        text = json.dumps(i, default=lambda o: o.__dict__, ensure_ascii=False)
        f.write(text + "\n")