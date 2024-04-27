import json
from classes.Path import *
from utils.fileProcessor import dataReader
from utils.promptExtract import promptExtract
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
    prompt = input("Enter the prompt: ")
    result = promptExtract(prompt, pathKeys) #, lng = 106.652565, lat = 10.75125313
    if result is not None:
        field, value, function = result
        chosenFunction = eval(f"path.{function}")
        res = chosenFunction(field, value)
        path.outputAsCSV(OUTPUT_FILENAME_CSV, res)
        path.outputAsJSON(OUTPUT_FILENAME_JSON, res)
    else :
        print("No result found, please try again.")