def solution(s):
    n = len(s)
    answer = [-1]*n
    for i in range(n):
        for j in range(i):
            if s[i]==s[j]:
                answer[i]=(i-j)
    return answer