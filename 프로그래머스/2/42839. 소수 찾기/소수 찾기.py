import math

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def dfs(numbers, number, s, visited, depth):
    if depth > len(numbers):
        return
    
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            s.add(int(number+numbers[i]))
            dfs(numbers, number+numbers[i], s, visited, depth+1)
            visited[i] = False
    
def solution(numbers):
    answer = 0
    s = set()
    visited = [False for _ in range(7)]
    
    dfs(numbers, "", s, visited, 0)
    
    for i in s:
        if check_prime(i):
            answer += 1

    return answer