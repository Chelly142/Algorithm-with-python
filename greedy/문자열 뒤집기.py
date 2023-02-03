s = input()

def serch_con(s):
    c=1
    l=[]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c+=1
        else:
            l.append(c)
            c = 1
    return l

result = len(serch_con(s))//2
print(result)

s = input()
flag = s[0]
answer=0
for i in s:
  if flag == i:
    continue
  else:
    answer+=1
if flag[0] ==flag[-1]:
  print(answer-1)
else:
  print(answer)
