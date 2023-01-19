def solution(s):
    answer = ''
    flag =True
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            flag = True
            continue
        else:
            if flag:
                s[i] = s[i].upper()
                flag = False
            else:
                s[i] = s[i].lower()
                flag = True
    return ''.join(s)
