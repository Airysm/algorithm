def solution(number, k):
    answer = ''
    stack = []
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    for s in stack[:len(number)-k]:
        answer += s
    
    return answer