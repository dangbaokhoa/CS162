import json
from utils.fileProcessor import dataReader
from classes.Path import *

INPUT_FILENAME = "paths.json"
OUTPUT_FILENAME_CSV = "paths.csv"
OUTPUT_FILENAME_JSON = "paths.json"

routesGroup = dataReader(INPUT_FILENAME)

def getListPath():
  res = list()
  for routes in routesGroup:
    if not routes:
      continue
    routes = json.loads(routes)
    res.append(Path(routes))
    
  listPath = PathQuery(res)
  return listPath

if __name__ == "__main__":
  path = getListPath()
  data = path.searchByLngLat(106.652565, 10.75125313)
  path.outputAsCSV(OUTPUT_FILENAME_CSV, data)
  path.outputAsJSON(OUTPUT_FILENAME_JSON, data)