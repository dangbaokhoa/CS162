import pyproj
def latlngToXY(lat, lng):
  wgs84 = pyproj.CRS("EPSG:4326")
  utm_vietnam = pyproj.CRS("EPSG:32648")

  transformer = pyproj.Transformer.from_proj(wgs84, utm_vietnam, always_xy=True)
  x, y = transformer.transform(lng, lat) 
  return (x, y)
