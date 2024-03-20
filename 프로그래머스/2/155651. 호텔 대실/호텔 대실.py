from heapq import *

def solution(book_time):
    book_minutes = [[0, 0] for _ in range(len(book_time))]
    heap = []
    
    for i, time in enumerate(book_time):
        t1 = time[0].split(':')
        t2 = time[1].split(':')
        book_minutes[i] = [int(t1[0])*60+int(t1[1]), int(t2[0])*60+int(t2[1])+10]
    
    book_minutes.sort(key=lambda x:x[0])
    
    for m1, m2 in book_minutes:
        if not heap:
            heappush(heap, m2)
            continue
        if heap[0] <= m1:
            heappop(heap)
        heappush(heap, m2)
                 
    return len(heap)