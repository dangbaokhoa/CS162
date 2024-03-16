import os
import json
FILEPATH = os.path.abspath("data/{}/{}")

FORDER_TYPE = {"input": "input", "output": "output"}

def dataReader(INPUT_FILENAME):
  with open(FILEPATH.format(FORDER_TYPE["input"], INPUT_FILENAME), 'r', encoding="UTF-8") as f:
    routesGroup = f.read().split("\n")
    return routesGroup
  
def dataWriterJSON(OUTPUT_FILENAME, data):
 with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
    json.dump(data, f, default=lambda x: x.__dict__, ensure_ascii=False)

def dataWriterCSV(OUTPUT_FILENAME, data):
  with open(FILEPATH.format(FORDER_TYPE["output"], OUTPUT_FILENAME), 'w', encoding="UTF-8") as f:
    for key in data[0].__dict__:
      f.write(key + ",")
    f.write("\n")
    for i in data:
      for route in i.__dict__.values():
        f.write(str(route) + ",")
      f.write("\n")
