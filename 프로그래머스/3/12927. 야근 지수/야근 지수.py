import heapq

def solution(n, works):
    answer = 0
    max_heap = []
    for item in works:
        heapq.heappush(max_heap, (-item, item))
    
    while n > 0:
        temp = heapq.heappop(max_heap)[1] - 1
        heapq.heappush(max_heap, (-temp, temp))
        n -= 1
    
    if max_heap[0][1] <= 0:
        return 0
    
    while max_heap:
        answer += heapq.heappop(max_heap)[1]**2
        
    return answer