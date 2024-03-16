import os
import json

from classes.RouteVar import RouteVar
from classes.RouteVarQuery import RouteVarQuery
from utils.fileProcessor import dataReader, dataWriterCSV, dataWriterJSON

INPUT_FILENAME = "vars.json"
OUTPUT_FILENAME_CSV = "output.vars.csv"
OUTPUT_FILENAME_JSON = "output.vars.json"

routesGroup = dataReader(INPUT_FILENAME)

res = list()
for routes in routesGroup:
  if (routes):
    routes = json.loads(routes)
    for route in routes:
      data = RouteVar(route)
      res.append(data)

hanldeRouteVar = RouteVarQuery(res) 

listRoute = hanldeRouteVar.searchByRouteId(5)

# Write CSV file
dataWriterCSV(OUTPUT_FILENAME_CSV, listRoute)

# Read CSV file
# with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_CSV), 'r', encoding="UTF-8") as f:
#   csv_reader = csv.reader(f)
#   for row in csv_reader:
#     print(row)
    
# Write JSON file
dataWriterJSON(OUTPUT_FILENAME_JSON, listRoute)
# Read JSON file
# with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME_JSON), 'r', encoding="UTF-8") as f:
#   data = json.load(f)
#   for route in data:
#     print(route)
  