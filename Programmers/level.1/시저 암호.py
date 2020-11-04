def solution(s, n):
    answer = ''
    print(ord('A'))
    for i in s:
        if i == ' ':
            c = ' '
        elif i.isupper():
            c = chr((ord(i)-65+n)%26+65)
        else:
            c = chr((ord(i)-97+n)%26+97)
        answer = answer + c
    return answer
