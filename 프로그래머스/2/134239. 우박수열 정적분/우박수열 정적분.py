def solution(k, ranges):
    answer = []
    list_k = []
    area = [0]
    count = 0
    
    while k > 1:
        temp = k
        if k%2 == 0:    k = k//2
        else:           k = k*3+1
        list_k.append((temp+k)/2)
        count += 1
    
    for i in range(len(list_k)):
        area.append(area[-1] + list_k[i])
    
    for r1, r2 in ranges:
        if r2 <= 0:
            r2 = r2+count
        if r1 == r2:
            answer.append(0.0)
        elif r1 > r2:
            answer.append(-1.0)
        else:
            answer.append(area[r2]-area[r1])
        
    return answer