def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month_day = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    answer = day[(sum(month_day[:a])+b)%7]
    return answer
