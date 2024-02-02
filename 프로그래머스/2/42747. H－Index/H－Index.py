def solution(citations):
    c = sorted(citations, reverse=True)
    answer = 0
    
    for i in range(len(c), 1, -1):
        h = 0
        for j in c:
            if i <= j:
                h += 1
        if h >= i:
            answer = i
            break
                
    return answer