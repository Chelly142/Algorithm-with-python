def solution(s):
    s = s.upper()
    print(s)
    if s.count('P') == s.count('Y'):
        answer = True
    else:
        answer = False
    return answer
