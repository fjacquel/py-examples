# -*- coding: utf-8 -*-
"""
JSON helper libary.

@author: Florian Jacquelet
"""

import json
import os.path
import codecs

def read_json(path):
  """ Read JSON file. """

  # Precondition
  if path is None or not os.path.isfile(path): return False

  # Read file
  with codecs.open(path, 'r', encoding='utf-8') as f:
    try:
      retval = json.load(f, encoding='utf-8')
    except Exception:
      retval = None

  return retval

def write_json(path, data):
  """ Write a JSON file. """

  status = False
  with codecs.open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
    status = True

  return status

if __name__ == '__main__':
  unit_conversion = {
      "temperature" : {
          "unit": "K",
          "uomsys": { "SI": "K", "ASMS": "°F", "SIP": "°C", "User defined" : "°C" },
          "conversion" : {
              "°C" : [ "-273.15", "1.0" ],
              "°F" : [ "-459.67", "1.8" ],
              "R" : [ "0.0", "1.8" ]
          }
      },
      "Δtemperature" : {
          "unit": "ΔK",
          "uomsys": { "SI": "ΔK", "ASMS": "Δ°F", "SIP": "Δ°C", "User defined" : "Δ°C" },
          "conversion" : {
              "Δ°C" : [ "0.0", "1.0" ],
              "Δ°F" : [ "0.0", "1.8" ],
              "ΔR"  : [ "0.0", "1.8" ]
          }
      },
      "dtemperature" : {
          "unit": "dK",
          "uomsys": { "SI": "dK", "ASMS": "d°F", "SIP": "d°C", "User defined" : "d°C" },
          "conversion" : {
              "d°C" : [ "0.0", "1.0" ],
              "d°F" : [ "0.0", "1.8" ],
              "dR"  : [ "0.0", "1.8" ]
          }
      }
  }

  write_json('example.json', unit_conversion)
  read_back = read_json('example.json')
  print('temperature in ' + read_back['temperature']['unit'])
