def solution(n):
    ans = 1
    
    while n > 1:
        ans += n % 2
        n = int(n / 2)

    return ans