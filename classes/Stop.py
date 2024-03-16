class Stop: 
  def __init__(self, route):
    for key, value in route.items():
      setattr(self, key, value)