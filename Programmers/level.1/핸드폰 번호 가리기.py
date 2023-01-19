def solution(phone_number):
    solution = []
    for i,v in enumerate(phone_number):
        if i < len(phone_number)-4:
            solution.append('*')
        else:
            solution.append(v)
    return ''.join(solution)
