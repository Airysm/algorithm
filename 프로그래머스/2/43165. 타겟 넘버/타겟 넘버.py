answer = 0

def dfs(numbers, target, count, num):
    global answer
    if len(numbers) == count and num == target:
        answer += 1
        return
    elif len(numbers) == count:
        return
    
    dfs(numbers, target, count+1, num + numbers[count])
    dfs(numbers, target, count+1, num - numbers[count])
    
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer