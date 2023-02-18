from collections import deque
def solution(n, computers):
    answer = 0
    check = [0]*n
    q = deque([])
    for i in range(n):
        if check[i]==1:
            continue
        q.append(computers[i])
        while q:
            now_nod = q.popleft()
            for index ,connection in enumerate(now_nod):
                if check[index]==0 and connection == 1:
                    check[index]=1
                    q.append(computers[index])
        answer+=1
            
        
    return answer
