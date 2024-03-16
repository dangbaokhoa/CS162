import json
from classes.RouteVar import RouteVar

class RouteVarQuery(RouteVar):
  def __init__(self, routes):
    self.routes = routes

  def searchByRouteId(self, routeId):
    # print(vars(self.routes[0]).keys())
    listRoute = []
    for route in self.routes:
      if route.RouteId == routeId:
        listRoute.append(route)
    return listRoute
  def searchByStopId(self, stopId):
    # print(vars(self.routes[0]).keys())
    listRoute = []
    for route in self.routes:
      if route.StopId == stopId:
        listRoute.append(route)
    return listRoute