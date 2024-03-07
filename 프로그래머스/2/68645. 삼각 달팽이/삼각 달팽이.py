import math

def solution(n):
    answer = []
    tri = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    
    if n == 1:
        return [1]
    
    num = 1
    i, j = 0, 0
    while True:
        while i < n and tri[i][j] == 0:
            tri[i][j] = num
            num += 1
            i += 1
        i -= 1
        j += 1
        if tri[i][j] != 0:  break
        while j < n and tri[i][j] == 0:
            tri[i][j] = num
            num += 1
            j += 1
        j -= 2
        i -= 1
        if tri[i][j] != 0:  break
        while i < n and j < n and tri[i][j] == 0:
            tri[i][j] = num
            num += 1
            i -= 1
            j -= 1
        i += 2
        j += 1
        if tri[i][j] != 0:  break
    
    for t in tri:
        for n in t:
            if n != 0:
                answer.append(n)
    
    return answer