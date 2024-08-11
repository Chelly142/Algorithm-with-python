import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    v,e = map(int, input().split())
    graph = {i:[] for i in range(1,v+1)}

    node_set1 = set()
    node_set2 = set()
    answer = "YES"
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    for node in range(1,v+1):
        if answer =="NO":
            break
        if node not in node_set1 and node not in node_set2:
            q = deque([(node,"set1")])
            node_set1.add(node)
            while q:
                now_node,set_type = q.popleft()
                if (set_type=="set1" and now_node in node_set2) or (set_type=="set2" and now_node in node_set1):
                    answer ="NO"
                    break
                for nxt_node in graph[now_node]:
                    if set_type=="set1":
                        if nxt_node not in node_set2:
                            node_set2.add(nxt_node)
                            q.append((nxt_node,"set2"))
                    if set_type=="set2":
                        if nxt_node not in node_set1:
                            node_set1.add(nxt_node)
                            q.append((nxt_node,"set1"))
            else:
                answer="YES"
    print(answer)