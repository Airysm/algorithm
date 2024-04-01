import heapq

def dijkstra(dist, nodes):
    heap = []
    heapq.heappush(heap, [1, 0])
    
    while heap:
        node, cost = heapq.heappop(heap)
        for n, c in nodes[node]:
            if cost + c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [n, cost+c])

def solution(N, road, K):
    answer = 0
    dist = [float('inf')]*(N+1)
    nodes = [[] for _ in range(N+1)]
    dist[1] = 0
    
    for r in road:
        nodes[r[0]].append([r[1], r[2]])
        nodes[r[1]].append([r[0], r[2]])
    
    dijkstra(dist, nodes)
    
    for d in dist:
        if d <= K:  answer += 1
        
    return answer