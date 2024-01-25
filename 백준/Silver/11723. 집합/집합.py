#2:52
import sys

m = int(sys.stdin.readline())

s =[]

sol=[]
for _ in range(m):
  op = sys.stdin.readline().strip().split()
  
  if len(op) == 1:
    if op[0] == "all":
      s = list(range(1,21))
    if op[0] == "empty":
      s=[]
      continue
  else:
    x = int(op[1])
    if op[0] == "add" and x not in s:
      s.append(x)
    if op[0] == "remove" and x in s:
      s.remove(x)
    if op[0] == "check":
      if x in s:
        print("1")
      else:
        print("0")
    if op[0] == "toggle":
      if x in s:
        s.remove(x)
      else:
        s.append(x)
  

