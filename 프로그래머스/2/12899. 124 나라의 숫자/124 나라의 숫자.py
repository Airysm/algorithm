def solution(n):
    num = ['4', '1', '2']
    answer = ""
    while n > 0:
        answer = num[n%3] + answer
        n = (n - 1) // 3
    
    return answer