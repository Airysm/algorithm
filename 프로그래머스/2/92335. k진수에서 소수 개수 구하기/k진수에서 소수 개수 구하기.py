import math

def check_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
        

def solution(n, k):
    answer = 0
    n_k = ""
    while n != 0:
        n_k = str(n % k) + n_k
        n = n//k
    
    for num in n_k.split('0'):
        if len(num) == 0:
            continue
        elif check_prime_num(int(num)):
            answer += 1
        
    return answer