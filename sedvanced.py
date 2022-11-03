#!/usr/bin/python3
import sys
import re

def replace(pattern,replaceto,filepath,count):
  with open(filepath) as f:
    content=f.read()

  content=re.sub(pattern, replaceto, content, count=count)

  with open(filepath,'w') as f:
    f.write(content)

  print(filepath)

if __main__=='__file__':
  pattern=sys.argv[1]
  replaceto=sys.argv[2]
  filepath=sys.argv[3]
  try:
    count=int(sys.argv[4])
  except IndexError:
    count=0

  replace(pattern,replaceto,filepath,count)
