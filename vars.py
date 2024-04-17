import json
from classes.RouteVar import * 
from utils.fileProcessor import dataReader
from utils.promptExtract import promptExtract
INPUT_FILENAME = "vars.json"
OUTPUT_FILENAME_CSV = "vars.csv"
OUTPUT_FILENAME_JSON = "vars.json"

routesGroup = dataReader(INPUT_FILENAME)

def getListRoute():
    listRoute = list()
    for routes in routesGroup:
        if (routes):
            routes = json.loads(routes)
            listRoute.append(RouteVar(routes))
        
    listRoute = RouteVarQuery(listRoute)

    return listRoute

if __name__ == "__main__": 
    route = getListRoute()
    prompt = input("Enter the prompt: ")
    result = promptExtract(prompt, routeKeys)
    if result is not None:
        field, value, function = result
        chosenFunction = eval(f"route.{function}")
        data = chosenFunction(field, value)
        route.outputAsCSV(OUTPUT_FILENAME_CSV, data)
        route.outputAsJSON(OUTPUT_FILENAME_JSON, data)
    else :
        print("No result found, please try again.")
    