def solution(clothes):
    d = dict()
    answer = 1
    
    for name, type_clo in clothes:
        if type_clo in d:   d[type_clo] += 1
        else:               d[type_clo] = 1
    
    for type_clo in d:
        answer *= d[type_clo] + 1
    answer -= 1
    return answer