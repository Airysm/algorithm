def solution(n,a,b):
    answer = 0
    a, b = a - 1, b - 1
    
    while a != b:
        a, b = int(a/2), int(b/2)
        answer += 1

    return answer