def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arr):
    answer = 0
    
    for i in arr:
        answer = i if answer == 0 else answer * i // gcd(answer, i)
    
    return answer