import json
from classes.RouteVar import * 
from utils.fileProcessor import dataReader

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
    data = route.searchByAttr("RouteId", 5)
    route.outputAsJSON(OUTPUT_FILENAME_JSON, data)
    route.outputAsCSV(OUTPUT_FILENAME_CSV, data)
