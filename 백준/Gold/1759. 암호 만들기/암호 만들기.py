

l , c = map(int,input().split())
alphabet = list(input().split())
alphabet.sort()
mom = 'aeiou'
def dfs(code):
  if len(code) == l:
    cnt = 0
    for i in code:
      if i in mom:
        cnt+=1
    if 0<cnt<(l-1):
      print(code)
  for a in alphabet:
    if code[-1] <a:
      dfs(code+a)
for a in alphabet:
  dfs(a)