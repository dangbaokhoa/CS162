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
  
  def searchByAttr(self, field, value):
    res = []
    for stops in self.stopGroup:
      for stop in stops.Stops:
        if (str(stop[field]) == value): 
          res.append({"Stop": stop, "RouteId": stops.RouteId, "RouteVarId": stops.RouteVarId})
    return res

  def searchByStopId(self, field, value):
    return self.searchByAttr(field, value)

  def searchByCode(self, field, value):
    return self.searchByAttr(field, value)

  def searchByName(self, field, value):
    return self.searchByAttr(field, value)

  def searchByStopType(self, field, value):
    return self.searchByAttr(field, value)

  def searchByZone(self, field, value):
    return self.searchByAttr(field, value)

  def searchByWard(self, field, value):
    return self.searchByAttr(field, value)

  def searchByAddressNo(self, field, value):
    return self.searchByAttr(field, value)

  def searchByStreet(self, field, value):
    return self.searchByAttr(field, value)

  def searchBySupportDisability(self, field, value):
    return self.searchByAttr(field, value)

  def searchByStatus(self, field, value):
    return self.searchByAttr(field, value)

  def searchByLng(self, field, value):
    return self.searchByAttr(field, value)

  def searchByLat(self, field, value):
    return self.searchByAttr(field, value)

  def searchBySearch(self, field, value):
    return self.searchByAttr(field, value)
    
  def searchByRoutes(self, field, value):
    return self.searchByAttr(field, value)
  
  def searchByAttrAdvance(self, field, value):
    res = []
    for stops in self.stopGroup:
      if (str(getattr(stops, field)) == value):
        res.append(stops.__dict__)
    return res
  
  def searchByRouteId(self, field, value):
    return self.searchByAttrAdvance(field, value)

  def searchByRouteVarId(self, field, value):
    return self.searchByAttrAdvance(field, value)

  def outputAsCSV(self, OUTPUT_FILENAME, res) -> None:
    if not res:
      return
    OUTPUT_FILE_PATH = os.path.abspath("output/{}")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
    with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
      f.write(",".join(stopKeys) + "\n")
      for stop in res:
        for i in stop.values():
          if (type(i) == dict):
            for j in i.values():
              f.write(str(j) + ",")
          else:
            f.write(str(i) + ",")
        f.write("\n")   

  def outputAsJSON(self, OUTPUT_FILENAME, res) -> None:
    if not res:
      return
    OUTPUT_FILE_PATH = os.path.abspath("output/{}")
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
    with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
      for i in res:
        text = json.dumps(i, default=lambda o: o.__dict__, ensure_ascii=False)
        f.write(text + "\n")