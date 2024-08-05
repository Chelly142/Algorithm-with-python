import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

#15:23
s = input().rstrip()
explosion_s = input().rstrip()

stack =[]
def can_explose():
    return stack[-len(explosion_s):]==list(explosion_s)
    
def explose():
    global stack
    for _ in range(len(explosion_s)):
      stack.pop()

for c in s:
    stack.append(c)
    if can_explose():
        explose()

if stack:print(*stack,sep="")
else:print("FRULA")