from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0 for _ in range(bridge_length)])
    q = deque(truck_weights)
    weight_sum = 0
    
    while q:
        time += 1
        
        weight_sum -= bridge.popleft()
        
        if weight_sum + q[0] <= weight:
            weight_sum += q[0]
            bridge.append(q.popleft())
        else:
            bridge.append(0)
            
    time += bridge_length
    
    return time