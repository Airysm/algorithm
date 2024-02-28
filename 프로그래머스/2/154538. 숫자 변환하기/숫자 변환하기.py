def solution(x, y, n):
    count = 0
    s = set()
    s.add(x)
    
    while s:
        if y in s:
            return count
        nv = set()
        
        for v in s:
            if v + n <= y:
                nv.add(v+n)
            if v * 2 <= y:
                nv.add(v*2)
            if v * 3 <= y:
                nv.add(v*3)
        s = nv
        count += 1
        
    return -1