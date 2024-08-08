import sys
input = sys.stdin.readline

n = int(input())
heighs = []
for _ in range(n):
    heighs.append(int(input()))

stack = []

answer = 0
equal_cnt = 0
for i in range(n):
    i_person = 1
    while stack and stack[-1][0]<=heighs[i]:
        heigh, person = stack.pop()
        answer+=person
        if heigh==heighs[i]:
            i_person=person+1
    if stack:
        answer+=1
    stack.append((heighs[i],i_person))
print(answer)