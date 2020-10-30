def solution(s):
    answer = True
    return s.isdigit() and (len(s)==4 or len(s)==6)
