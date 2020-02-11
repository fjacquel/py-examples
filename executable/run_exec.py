# -*- coding: utf-8 -*-
"""
Call an executable

@author: Florian Jacquelet
"""

import subprocess
import sys
import threading


def transfer(proc, instream, outstream):
  """ Transfer process data stream to another """
  out = ' '
  while out != '' or proc.poll() is None:
    out = instream.read()
    if out == b'': break

    outstream.write(out.decode())
    outstream.flush()


def exec_command(command, directory=None):
  """ Execute specified command """

  # Create process
  proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory)

  # Create stream handling thread (Redirect messages to stdout)
  out_thread = threading.Thread(name='stdout_transfer', target=transfer, args=(proc, proc.stdout, sys.stdout))
  err_thread = threading.Thread(name='stderr_transfer', target=transfer, args=(proc, proc.stderr, sys.stdout))
  err_thread.start()
  out_thread.start()
  out_thread.join()
  err_thread.join()

# ----------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------

if __name__ == '__main__':
  print(exec_command('ipconfig'))
