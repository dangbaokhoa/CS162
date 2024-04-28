import json

from classes.Stop import *
from utils.fileProcessor import *

INPUT_FILENAME = "stops.json"
OUTPUT_FILENAME_CSV = "stops.csv"
OUTPUT_FILENAME_JSON = "stops.json"
stopsGroup = dataReader(INPUT_FILENAME)

def getListStop():
    res = list()
    for stops in stopsGroup:
        if not stops:
            continue
        stops = json.loads(stops)
        res.append(Stop(stops))
    
    listRoutes = StopQuery(res)
    return listRoutes

if __name__ == "__main__": 
    stop = getListStop()
    # Search by StopId
    res = stop.searchByStopId("StopId", "10")
    stop.outputAsCSV(OUTPUT_FILENAME_CSV, res)
    stop.outputAsJSON(OUTPUT_FILENAME_JSON, res)