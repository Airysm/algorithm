def solution(order):
    result = 0
    basic = []
    stack = []
    
    for i in range(len(order), 0, -1):
        basic.append(i)
    
    for i in range(len(order)):
        while basic and basic[-1] < order[i]:
            stack.append(basic.pop())
        if basic and basic[-1] == order[i]:
            basic.pop()
            result += 1
        elif stack and stack[-1] == order[i]:
            stack.pop()
            result += 1
        else:
            break
            
            
    return result