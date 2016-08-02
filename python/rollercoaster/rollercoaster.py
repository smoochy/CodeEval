#!/usr/bin/python

import sys
import re

# check that a filename argument was provided, otherwise
if len(sys.argv) < 2:
  raise Exception("Filename must be first argument provided")

filename = sys.argv[1]
lines = []

# open file in read mode, assuming file  is in same directory as script
try:
  file = open(filename, 'r')

  # read Fibbonacci indexes from file into list
  lines = file.readlines()
  file.close()
except IOError:
  print "File '%s' was not found in current directory" % filename

lines = [line.replace('\n', '') for line in lines]

try:
  lines.remove("")
except:
  pass

import collections

for line in lines:
    toUpper = True
    chars = list(line)
    for index, char in enumerate(chars):
        if char.isalpha():
            if toUpper:
                chars[index] = char.upper()
            else:
                chars[index] = char.lower()
            toUpper = not toUpper
    print ''.join(chars)
