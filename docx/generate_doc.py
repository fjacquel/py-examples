# -*- coding: utf-8 -*-
"""
Example Python file generating a document from a template.

@author: Florian Jacquelet
"""

from __future__ import print_function

import copy
import sys
import os.path
import json
import codecs
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage, RichText

# ----------------------------------------------------------------------------
# JSON reading function
# ----------------------------------------------------------------------------

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

def get_full_path(path):
  """ Return absolute path based on the current script. """
  if not path: return path
  return os.path.join(os.path.dirname(sys.argv[0]), path)

# ----------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------

if __name__ == '__main__':
  template_path  = get_full_path(r'template.docx')
  generated_path = get_full_path(r'generated.docx')
  context_path   = get_full_path(r'inject.json')

  # Open document
  doc = DocxTemplate(template_path)

  # Read context
  replacements = read_json(context_path)

  # Replace variable
  context = copy.copy(replacements['variables'])

  # Replace images
  for image, data in replacements['images'].items():
    context[image] = InlineImage(doc, data[0], width=Mm(data[1]))

  # Replace URLs
  for url, data in replacements['urls'].items():
    rt = RichText()
    rt.add(data[0], url_id=doc.build_url_id(data[1]))
    context[url] = rt

  # Replace tables
  for table, data in replacements['tables'].items():
    context[table + '_col_labels'] = data['col_labels']
    context[table + '_tbl_contents'] = data['tbl_contents']

  # Save new file
  doc.render(context)
  doc.save(generated_path)
