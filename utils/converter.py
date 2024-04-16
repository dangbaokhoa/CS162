import pyproj

wgs84 = pyproj.CRS("EPSG:4326")
utm_vietnam = pyproj.CRS("EPSG:3405")
transformer = pyproj.Transformer.from_proj(wgs84, utm_vietnam, always_xy=True)

def lnglatToXY(lng, lat):
  if not lng or not lat:
    return (None, None)
  x, y = transformer.transform(lng, lat) 
  return (x, y)