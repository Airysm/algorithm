count = 0

def solution(n, wires):
    answer = n
    visited = [0 for _ in range(n+1)]
    nodes = [[] for _ in range(n+1)]
    
    for wire in wires:
        visited[wire[0]] += 1
        visited[wire[1]] += 1
        nodes[wire[0]].append(wire[1])
        nodes[wire[1]].append(wire[0])
    
    def dfs(wire):
        global count
        count += visited[wire[0]] - 1
        for node in nodes[wire[0]]:
            if wire[1] != node:
                dfs([node, wire[0]])
    
    for wire in wires:
        global count
        dfs(wire)
        count += 1
        min_wire = abs(n-count-count)
        count = 0
        answer = min(answer, min_wire)
        
    return answer