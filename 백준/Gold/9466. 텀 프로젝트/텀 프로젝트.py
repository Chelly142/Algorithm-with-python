import sys
sys.setrecursionlimit(111111) 
input = sys.stdin.readline

#12:43

def solution(n, prefer_list):
    visited = [False]*(n+1)
    finished = [False]*(n+1)

    def dfs(node):
        nxt = prefer_list[node]
        if finished[node]:
            return 0
        elif visited[node]: #사이클인 경우
            cycle_size = 1
            while nxt!=node:
                cycle_size+=1
                nxt = prefer_list[nxt]
            return cycle_size
        visited[node] = True
        cycle_size = dfs(nxt)
        finished[node] = True
        
        return cycle_size
    answer = n
    for i in range(1,n+1):
        if not finished[i]:
            answer -= dfs(i)
    return answer

t = int(input())
for _ in range(t):
    n = int(input())
    prefer_list = [0]+list(map(int, input().split()))
    print(solution(n, prefer_list))