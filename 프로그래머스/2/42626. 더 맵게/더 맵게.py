import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville:
        temp = heapq.heappop(scoville)
        if temp >= K:
            break
        elif not scoville and temp < K:
            return -1
        heapq.heappush(scoville, temp + heapq.heappop(scoville) * 2)
        count += 1
    return count