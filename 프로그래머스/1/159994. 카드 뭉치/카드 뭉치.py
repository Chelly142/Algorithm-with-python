from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cards1=deque(cards1)
    cards2=deque(cards2)
    c1=cards1.popleft()
    c2=cards2.popleft()
    for word in goal:
        if word == c1:
            if cards1:
                c1=cards1.popleft()
        elif word == c2:
            if cards2:
                c2=cards2.popleft()
        else:
            return 'No'
    return 'Yes'