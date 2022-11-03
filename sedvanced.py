import sys
import re

pattern=sys.argv[1]
replaceto=sys.argv[2]
filepath=sys.argv[3]
try:
  count=int(sys.argv[4])
except IndexError:
  count=0

with open(filepath) as f:
  content=f.read()

content=re.sub(pattern, replaceto, content, count=count)

with open(filepath) as f:
  f.write(content)
