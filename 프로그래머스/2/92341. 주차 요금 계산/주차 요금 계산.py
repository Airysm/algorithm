import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    d = defaultdict(list)
    
    for record in records:
        time, car, inout = record.split()
        minutes = int(time[:2]) * 60 + int(time[3:])
        d[car].append(minutes)
    
    cars = sorted(d.keys())
    
    for c in cars:
        if len(d[c]) % 2 == 1:
            d[c].append(23*60+59)
    
    for c in cars:
        minute = sum(d[c][1::2]) - sum(d[c][::2])
        if minute > fees[0]:
            money = fees[1] + math.ceil((minute-fees[0])/fees[2]) * fees[3]
        else:
            money = fees[1]
        answer.append(money)
        
    return answer