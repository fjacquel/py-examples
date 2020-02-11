# -*- coding: utf-8 -*-
"""
Excel helper libary.

See https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

@author: Florian Jacquelet
"""

import sys
import os.path
import pandas
import matplotlib.pyplot as plt

def get_full_path(file_path):
  """ Return absolute path based on the current script. """
  if not file_path: return file_path
  return os.path.join(os.path.dirname(sys.argv[0]), file_path)

if __name__ == '__main__':
  # Open file
  path  = get_full_path('sales.xlsx')
  image = get_full_path('sales.jpg')
  data_frame = pandas.read_excel(path, sheet_name='Sales')

  # Who sold the most pencils?
  # 1. Get all pencils data
  pencils = data_frame[data_frame['Item'] == 'Pencil']
  print(pencils)
  # 2. Group by Sales guy
  data = pencils.groupby('Sales').sum()
  print(data)
  # 3. Sort by Units
  data_byunits = data.sort_values(by='Units', ascending=False)
  print(data_byunits.head(1).index[0] + ' sold the most units')  # Row index is the Rep due to the grouping
  # 3. Sort by Cash = Total
  data_bycash  = data.sort_values(by='Cash', ascending=False)
  print(data_bycash.head(1).index[0] + ' brought the most cash') # Row index is the Rep due to the grouping

  # 4. Plot data
  plot = data_bycash.plot.bar(y='Cash')
  fig = plot.get_figure()
  plt.title('Best sales guy')
  plt.xlabel('Sales representative')
  plt.ylabel('CHF')
  fig.subplots_adjust(bottom=0.22) # Increase space for label
  fig.savefig(image)
