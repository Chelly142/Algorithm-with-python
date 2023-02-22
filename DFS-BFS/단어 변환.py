from collections import deque
def solution(begin, target, words):
    answer = 0
    #bfs로 모든 words의 요소에 대해 참조해야 풀수있다.
    #words 요소를 사용할때마다 사용했다는 check 을 해주는 words_check 리스트를 초기화
    #현재 단어 기준으로 하나만 다른 녀석들을 큐에 넣고 재귀로 돌려준다면? 깔끔할듯
    q = deque([])
    q.append(begin)
    words.append(begin)
    words_check = [0]*len(words)
    if target not in words:
        return 0
    while q:
        n_w = q.popleft()
        
        for i in words:
            c=0
            if words_check[words.index(i)]!=0:
                continue
            for x,y in zip(i,n_w):
                if x!=y:
                    c+=1
            if c==1:
                words_check[words.index(i)]=words_check[words.index(n_w)]+1
                if i == target:
                    return words_check[words.index(target)]
                q.append(i)
        print(words_check)
    return words_check[words.index(target)]
