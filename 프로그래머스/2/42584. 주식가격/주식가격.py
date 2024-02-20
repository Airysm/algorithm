def solution(prices):
    flag = True
    answer = []
    
    for i in range(len(prices)):
        sec = -1
        for j in range(i, len(prices)):
            sec += 1
            if prices[i] > prices[j]:
                answer.append(sec)
                flag = False
                break
        if flag:
            answer.append(sec)
        else:
            flag = True
            
    return answer