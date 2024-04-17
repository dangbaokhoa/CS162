import pyproj
import os
import json
wgs84 = pyproj.CRS("EPSG:4326")
utm_vietnam = pyproj.CRS("EPSG:3405")
transformer = pyproj.Transformer.from_proj(wgs84, utm_vietnam, always_xy=True)
OUTPUT_FILE_PATH = "output/{}"
def lnglatToXY(lng, lat):
  if not lng or not lat:
    return (None, None)
  x, y = transformer.transform(lng, lat) 
  return (x, y)

def outputAsJSON(OUTPUT_FILENAME, res):

  os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)

  with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
    json.dump(res, f, default=lambda x: x.__dict__, ensure_ascii=False)

def outputAsCSV(OUTPUT_FILENAME, res):

  os.makedirs(os.path.dirname(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME)), exist_ok=True)

  with open(OUTPUT_FILE_PATH.format(OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
    if not res:
      return
    for i in range(len(res)):
      if type(res[i]) != dict:
        res[i] =  res[i].__dict__

    for key in res[0].keys():
      f.write(key + ",")
    f.write("\n")
    for i in res:
      for route in i.values():
        f.write(str(route) + ",")
      f.write("\n")