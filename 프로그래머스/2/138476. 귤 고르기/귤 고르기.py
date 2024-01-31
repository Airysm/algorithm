def solution(k, tangerine):
    d = dict()
    answer = 0
    count = 0
    
    for i in tangerine:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1 
            
    d = dict(sorted(d.items(), key = lambda x : x[1], reverse=True))
    
    for i in d:
        if k <= count:
            break
        count += d[i]
        answer += 1
        
    return answer