#!/usr/bin/python3
import sys
import re

def sed(pattern,replaceto,filepath,count=0):
  with open(filepath) as f:
    content=f.read()

  content=re.sub(pattern, replaceto, content, count=count)

  with open(filepath,'w') as f:
    f.write(content)

if __file__=='__main__':
  pattern=sys.argv[1]
  replaceto=sys.argv[2]
  filepath=sys.argv[3]
  try:
    count=int(sys.argv[4])
  except IndexError:
    count=0

  sed(pattern,replaceto,filepath,count=count)
  print(filepath)
