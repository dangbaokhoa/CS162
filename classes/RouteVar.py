keys = ["RouteId", "RouteVarId", "RouteVarName", "RouteVarShortName", "RouteNo", "StartStop", "EndStop", "Distance", "Outbound", "RunningTime"]

class RouteVar: 
  def __init__(self, route):
    for key, value in route.items():
      setattr(self, key, value)
  @property
  def getRouteId(self):
    return self.RouteId

  @property
  def getRouteVarId(self):
    return self.RouteVarId

  @property
  def getRouteVarName(self):
    return self.RouteVarName

  @property
  def getRouteVarShortName(self):
    return self.RouteVarShortName

  @property
  def getRouteNo(self):
    return self.RouteNo

  @property
  def getStartStop(self):
    return self.StartStop

  @property
  def getEndStop(self):
    return self.EndStop

  @property
  def getDistance(self):
    return self.Distance

  @property
  def getOutbound(self):
    return self.Outbound

  @property
  def getRunningTime(self):
    return self.RunningTime
  
  # @RouteId.setter
  # def RouteId(self, value):
  #   self.RouteId = value

  # @RouteVarId.setter
  # def RouteVarId(self, value):
  #   self.RouteVarId = value

  # @RouteVarName.setter
  # def RouteVarName(self, value):
  #   self.RouteVarName = value

  # @RouteVarShortName.setter
  # def RouteVarShortName(self, value):
  #   self.RouteVarShortName = value

  # @RouteNo.setter
  # def RouteNo(self, value):
  #   self.RouteNo = value

  # @StartStop.setter
  # def StartStop(self, value):
  #   self.StartStop = value

  # @EndStop.setter
  # def EndStop(self, value):
  #   self.EndStop = value

  # @Distance.setter
  # def Distance(self, value):
  #   self.Distance = value

  # @Outbound.setter
  # def Outbound(self, value):
  #   self.Outbound = value

  # @RunningTime.setter
  # def RunningTime(self, value):
  #   self.RunningTime = value
    