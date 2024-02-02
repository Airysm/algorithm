from collections import deque

def solution(cacheSize, cities):
    d = deque()
    time = 0
    
    for city in cities:
        city = city.upper()
        if city in d:
            d.remove(city)
            time += 1
        else:   time += 5
        d.append(city)
        
        if len(d) > cacheSize:
            d.popleft()
                              
    return time