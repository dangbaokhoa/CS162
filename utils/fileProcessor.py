import os

INPUT_FILE_PATH = os.path.abspath("data/{}")
OUTPUT_FILE_PATH = os.path.abspath("output/{}")

def dataReader(INPUT_FILENAME):
  with open(INPUT_FILE_PATH.format(INPUT_FILENAME), 'r', encoding="UTF-8") as f:
    data = f.read().split("\n")
    return data