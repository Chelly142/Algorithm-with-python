# 인접 리스트로 초기화해주고 만약 갈 곳 없으면 백트래킹
# dfs
def solution(tickets):
    answer = []
    graph = {}

    # 1. 딕셔너리 초기화 (동생이 짠 코드 그대로!)
    for u, v in tickets:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        
    # 2. 도착지 알파벳 순으로 정렬 (알파벳이 앞서는 곳부터 탐색하기 위해)
    for u in graph:
        graph[u].sort()
        
    # 총 방문해야 할 도시의 수 = 티켓 수 + 1
    total_len = len(tickets) + 1
    
    def dfs(now, path):
        if len(path)==total_len:
            return path
        if now not in graph or not graph[now] :
            return False
            
        for i,nxt in enumerate(graph[now]):
            graph[now].pop(i)
            path.append(nxt)
            p = dfs(nxt, path)
            if p:
                return p
            path.pop()
            graph[now].insert(i, nxt)
        return False
    answer = dfs("ICN",["ICN"])
    return answer