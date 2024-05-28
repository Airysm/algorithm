def solution(prices):
    flag = True
    answer = []
    
    for i in range(len(prices)):
        sec = -1
        for j in range(i, len(prices)):
            sec += 1
            if prices[i] > prices[j]:
                break
        answer.append(sec)
            
    return answer