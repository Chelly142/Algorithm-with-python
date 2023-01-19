N = int(input())
mw = []
for i in range(N):
    mw.append(int(input()))
k = [0]*(max(mw)+1)
for i in mw:
    k[i] += 1


answer = 0
for i in range(len(k)):
    if answer < i*sum(k[i:]):
        answer = i*sum(k[i:])
print(answer)
