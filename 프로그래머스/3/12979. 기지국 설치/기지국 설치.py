import math

def solution(n, stations, w):
    answer = 0
    now = 1
    
    for station in stations:
        if station-w-now > 0:
            answer += math.ceil((station-w-now)/(w*2+1))
        now = station + w + 1
    
    if n-now+1 > 0:
        answer += math.ceil((n-now+1)/(w*2+1))
            
    return answer