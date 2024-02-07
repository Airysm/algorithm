import heapq

def solution(operations):
    q = []
    for operation in operations:
        if operation == "D -1":
            if q:
                heapq.heappop(q)
        elif operation == "D 1":
            if q:
                q.remove(max(q))
        elif operation[0] == 'I':
            heapq.heappush(q, int(operation[2:]))
    
    if not q:
        answer = [0, 0]
    else:
        answer = [max(q), heapq.heappop(q)]
        
    return answer
                           