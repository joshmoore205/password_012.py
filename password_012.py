#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip()
  level = [0, 0, 0, 0]
  for char in line:
    if char.islower():
      level[0] = 1
    elif char.isupper():
      level[1] = 1
    elif char.isdigit():
      level[2] = 1
    else:
      level[3] = 1
  print(sum(level))
