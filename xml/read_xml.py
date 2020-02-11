# -*- coding: utf-8 -*-
"""
Example Python file reading XML files

@author: Florian Jacquelet
"""

from __future__ import print_function
import os.path
import xml.etree.ElementTree as ET
import json

# ----------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------

if __name__ == '__main__':
  # Paths
  alpro_path  = r'c:\Data\ALPRO\6.18 Admin'
  output_path = alpro_path + r'\parameters.json'
  suffix = r'_definitions.xml'

  # Scan tech dir
  rootabs = os.path.abspath(alpro_path + r'\Technologies')
  index = 0

  # Generate the map
  retval = {}
  for parent, _, files in os.walk(rootabs):
    for f in files:
      def_path = os.path.join(parent, f)
      if not def_path.lower().endswith(suffix): continue

      # Read XML
      tree = ET.parse(def_path)
      root = tree.getroot() # definition
      for fe_node in root:
        fe_name = fe_node.attrib.get('type', f[:len(suffix)])
        params = {}
        for param_node in fe_node:
          param_idx  = param_node.attrib['index']
          param_name = param_node.attrib['name']
          params[param_name] = param_idx

        if retval.get(fe_name, None): print('Duplicate data for ' + fe_name)
        if len(params.keys()) < 1: continue
        retval[fe_name] = params

  # Write file
  with open(output_path, mode='w', encoding='utf-8') as stream:
    json.dump(retval, stream)
