import json
from utils.fileProcessor import dataReader, dataWriterJSON, dataWriterCSV
from utils.converter import latlngToXY

from classes.Stop import Stop
from classes.StopQuery import StopQuery

INPUT_FILENAME = "test.stops.json"
OUTPUT_FILENAME_CSV = "output.stops.csv"
OUTPUT_FILENAME_JSON = "output.stops.json"

routesGroup = dataReader(INPUT_FILENAME)

res = list()
for routes in routesGroup:
  routes = json.loads(routes)
  res.append(Stop(routes))

for i in res:
  for j in i.Stops:
    if "Lat" in j and "Lng" in j:
      x, y = latlngToXY(j["Lat"], j["Lng"])
      print(x, y)

# # Write CSV file
# with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_CSV), 'w', encoding="UTF-8") as f:
#   f.write("RouteId,StopId,StopName,StopShortName,RouteNo,StartStop,EndStop,Distance,Outbound,RunningTime\n")
#   for route in listRoute:
#     f.write("{},{},{},{},{},{},{},{},{},{}\n".format(route.RouteId, route.RouteVarId, route.RouteVarName, route.RouteVarShortName, route.RouteNo, route.StartStop, route.EndStop, route.Distance, route.Outbound, route.RunningTime))
    
# # Write JSON file
# with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_JSON), 'w', encoding="UTF-8") as f:
#   json.dump(listRoute, f, default=lambda x: x.__dict__, ensure_ascii=False)


