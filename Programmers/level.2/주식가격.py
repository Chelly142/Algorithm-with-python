def solution(prices):
    answer = list(range(len(prices)-1,-1,-1))
    stack = []
    stack.append([0,0])
    for i,v in enumerate(prices):
        pre = stack.pop()
        while v<pre[1]:
            answer[pre[0]] = i - pre[0]
            pre = stack.pop()
        stack.append(pre)
        stack.append([i,v])
    return answer
