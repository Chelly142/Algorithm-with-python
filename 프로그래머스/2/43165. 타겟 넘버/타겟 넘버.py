def solution(numbers, target):
    answer = 0
    depth = 1
    n = len(numbers)
    mask = 2**n
    for i in range(mask):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s+=numbers[j]
            else:
                s-=numbers[j]
        if s==target:
            answer+=1
        
    return answer