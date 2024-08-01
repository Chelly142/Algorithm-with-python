import sys
sys.setrecursionlimit(111111) 
input = sys.stdin.readline

#12:43
t = int(input())




for i in range(t):

    n = int(input())
    answer = n
    prefer_list = list(map(int,input().split()))
    prefer_dict = {i+1:prefer_list[i] for i in range(n)}
    visited = set()
    route =[]

    def dfs(node):
        global answer
        visited.add(node)
        route.append(node)
        nxt = prefer_dict[node]
        if nxt in visited:
            if nxt in route:
                answer -= len(route[route.index(nxt):])
        else:
            dfs(nxt)
    
    for i in range(1,n+1):
        if i not in visited:
            route =[]
            dfs(i)
    print(answer)
# 13:18 시간초과