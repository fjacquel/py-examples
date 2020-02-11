# -*- coding: utf-8 -*-
"""
Example downloading a file

Created on Tue Aug 11 08:30:10 2015

@author: Florian Jacquelet
Not Confidential
"""

import os
import urllib.request

# ----------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------

def download_file(url, target_path):
  """ Method downloading a single file.

      url: The URL pointing to a file.
      target_path: The target path where to save the file.
      headers: Extra readers required for the request.

      return True for success, False otherwise.
  """

  # Precondition
  if not url or not target_path: return False
  urllib.request.urlretrieve(url, target_path)

  return True

# ----------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------

if __name__ == '__main__':
  # Configuration
  url_example = 'https://morningstoryanddilbert.files.wordpress.com/2014/04/473-strip.gif'
  temp_path = r'C:\temp\download.jpg'
  # Download
  download_file(url_example, temp_path)
  # Open image
  os.startfile(temp_path)
