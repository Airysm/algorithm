def solution(elements):
    s = set()
    elements_len = len(elements)
    elements *= 2
    
    for i in range(elements_len):
        for j in range(elements_len):
            s.add(sum(elements[i:i+j+1]))
    
    return len(s)