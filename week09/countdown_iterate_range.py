#!/usr/bin/env python
"""
A countdown program similar to last week's, this time iterating a range object.
"""

__author__ = 'Jeffrey Bergamini for CS 12P, jeffrey.bergamini@cabrillo.edu'

import sys
import time

# sys.argv is a list of the command-line arguments included when running the program.
# https://docs.python.org/3/library/sys.html#sys.argv
print('Contents of sys.argv:', sys.argv, file=sys.stderr)

# Get an iterator for a range object starting at the user's chosen number, decreasing by 1 until 1
counter = (range(int(sys.argv[1]), 0, -1))

for num in counter:  # Flow jumps here when next() raises a StopIteration exception (i.e. range is exhausted)
  print(f'{num}{"." * num}')
  time.sleep(1)

print('Liftoff!')