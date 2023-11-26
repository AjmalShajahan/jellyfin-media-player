#!/usr/bin/env python -u

# simple script that takes data on stdin and outputs bz2 compressed data
# just to avoid having to install bzip2.exe on windows platforms

import bz2, os, sys

bufsize=4096

if __name__ == "__main__":
  compress = bz2.BZ2Compressor()
  while data := sys.stdin.read(bufsize):
    if cdata := compress.compress(data):
      sys.stdout.write(cdata)
  if cdata := compress.flush():
    sys.stdout.write(cdata)
