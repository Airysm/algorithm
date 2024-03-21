from collections import defaultdict

def solution(weights):
    count = 0
    d = defaultdict(float)
    ratio = [1, 1/2, 2, 2/3, 3/2, 3/4, 4/3]
    
    for w in weights:
        for r in ratio:
            count += d[r*w]
        d[w] += 1
        
    return int(count)