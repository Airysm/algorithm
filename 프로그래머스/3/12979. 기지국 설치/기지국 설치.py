def solution(n, stations, w):
    answer = 0
    now = 1
    
    for station in stations:
        length = station - w - now
        if length > 0:
            answer += length//(w*2+1) 
            if length%(w*2+1):
                answer += 1
        now = station + w + 1
    
    if n - now + 1 > 0:
        answer += (n-now+1)//(w*2+1)
        if (n-now+1)%(w*2+1):
            answer += 1
            
    return answer