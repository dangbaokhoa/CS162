import os
import json
import csv
from classes.RouteVar import RouteVar
from classes.RouteVarQuery import RouteVarQuery

INPUT_FILENAME = "test.json"
FILEPATH = os.path.abspath("data/{}/{}")
FORDER_TYPE = {"input": "input", "output": "output"}
OUTPUT_FILENAME_CSV = "output.csv"
OUTPUT_FILENAME_JSON = "output.json"

try: 
  with open(FILEPATH.format(FORDER_TYPE["input"], INPUT_FILENAME), 'r', encoding="UTF-8") as f:
    routesGroup = f.read().split("\n")

  res = list()
  for routes in routesGroup:
    if (routes):
      routes = json.loads(routes)
      for route in routes:
        data = RouteVar(route)
        res.append(data)
  
  hanldeRouteVar = RouteVarQuery(res) 
  
  listRoute = hanldeRouteVar.searchByRouteId(3)

  # Write CSV file
  with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_CSV), 'w', encoding="UTF-8") as f:
    f.write("RouteId,RouteVarId,RouteVarName,RouteVarShortName,RouteNo,StartStop,EndStop,Distance,Outbound,RunningTime\n")
    for route in listRoute:
      f.write("{},{},{},{},{},{},{},{},{},{}\n".format(route.RouteId, route.RouteVarId, route.RouteVarName, route.RouteVarShortName, route.RouteNo, route.StartStop, route.EndStop, route.Distance, route.Outbound, route.RunningTime))

  # Read CSV file
  # with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_CSV), 'r', encoding="UTF-8") as f:
  #   csv_reader = csv.reader(f)
  #   for row in csv_reader:
  #     print(row)
      
  # Write JSON file
  with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_JSON), 'w', encoding="UTF-8") as f:
    json.dump(listRoute, f, default=lambda x: x.__dict__, ensure_ascii=False)
  # Read JSON file
  # with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_JSON), 'r', encoding="UTF-8") as f:
  #   data = json.load(f)
  #   for route in data:
  #     print(route)
except ValueError as e:
  print("Error: ", e)
  