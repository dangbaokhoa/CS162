import os
import json
routeKeys = ["RouteId", "RouteVarId", "RouteVarName", "RouteVarShortName", "RouteNo", "StartStop", "EndStop", "Distance", "Outbound", "RunningTime"]
class RouteVar:
    def __init__(self, routes):
        self.routeVar = routes
          
    def setProperty(self, key, value):
        setattr(self, key, value)

    def getProperty(self, key):
        return getattr(self, key)

class RouteVarQuery():
    def __init__(self, routeGroup):
        self.routeGroup = routeGroup

    def searchByAttr(self, field, value):
        res = []
        for routes in self.routeGroup:
            for route in routes.routeVar:
                if (route[field] == value):
                    res.append(route)
        return res

    def outputAsCSV(self, OUTPUT_FILENAME, result) -> None:
        if not result:
            return
        OUTPUT_FILE_PATH = os.path.abspath("output/{}")
        os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
        with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
            f.write(",".join(routeKeys) + "\n")
            f.write("\n")
            for i in result:
                for route in i.values():
                    f.write(str(route) + ",")
                f.write("\n")

    def outputAsJSON(self, OUTPUT_FILENAME, result) -> None:
        OUTPUT_FILE_PATH = os.path.abspath("output/{}")
        os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)
        with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
            for i in result:
                i = [i]
                text = json.dumps(i, default=lambda o: o.__dict__, ensure_ascii=False)
                f.write(text + "\n")
