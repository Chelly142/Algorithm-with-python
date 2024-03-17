from collections import deque
def solution(arr):
    answer = [0,0]
    n=len(arr)
    q=deque()
    q.append((0,0,n))
    while q:
        x,y,s = q.popleft()
        k = arr[x][y]
        flag =False
        for i in range(s):
            for j in range(s):
                if k!= arr[x+i][y+j]:
                    flag = True
                    break
            if flag:
                break
        else:
            answer[k]+=1  
        if flag:
            q.append((x,y,s//2))
            q.append((x+s//2,y,s//2))
            q.append((x,y+s//2,s//2))
            q.append((x+s//2,y+s//2,s//2))
            
    return answer