import os
import json
stopKeys = ["StopId", "Code", "Name", "StopType", "Zone", "Ward", "AddressNo", "Street", "SupportDisability", "Status", "Lng", "Lat", "Search", "Routes", "RouteId", "RouteVarId"]
class Stop: 
  def __init__(self, stops):
    for key, value in stops.items():
      setattr(self, key, value)
      
  def setProperty(self, key, value):
    setattr(self, key, value)

  def getProperty(self, key):
    return getattr(self, key)
class StopQuery():
  def __init__(self, stopGroup):
    self.stopGroup = stopGroup

  def searchByAttr(self, **kwargs):
    key, value = list(kwargs.items())[0]
    res = []
    for stops in self.stopGroup:
      for stop in stops.Stops:
        if (stop[key] == value): 
          res.append({"Stop": stop, "routeId": stops.RouteId, "routeVarId": stops.RouteVarId})
          break
    return res

  def outputAsCSV(self, OUTPUT_FILENAME, data):
    if not data:
      return
    # print(data)
    OUTPUT_FILE_PATH = os.path.abspath("output/{}")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
    with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
      f.write(",".join(stopKeys) + "\n")
      for stop in data:
        for i in stop.values():
          if (type(i) == dict):
            for j in i.values():
              f.write(str(j) + ",")
            continue
          f.write(str(i) + ",")
        f.write("\n")   

  def outputAsJSON(self, OUTPUT_FILENAME, data):
    OUTPUT_FILE_PATH = os.path.abspath("output/{}")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
    with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
      for i in data:
        if (type(i) == dict):
          f.write(json.dumps(i, default=lambda o: o.__dict__, ensure_ascii=False) + "\n")
        text = json.dumps(i, default=lambda o: o.__dict__, ensure_ascii=False)
        f.write(text + "\n")