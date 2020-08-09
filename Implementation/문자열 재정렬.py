s = input()
a=0
result = []
for i in s:
    if i.isalpha():
        result.append(i)
    else:
        a += int(i)
result.sort()
if a:
    result.append(str(a))

print(''.join(result))
