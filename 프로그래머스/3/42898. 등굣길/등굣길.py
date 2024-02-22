def solution(m, n, puddles):
    grid = [
        [-1 for _ in range(m+1)]
        for _ in range(n+1)
    ]
    
    grid[1][1] = 1
    
    for i, j in puddles:
        grid[j][i] = 0
    
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                    grid[i][j] = 0
            elif grid[i][j] == -1:
                grid[i][j] = (grid[i-1][j] + grid[i][j-1]) % 1000000007
                
    return grid[-1][-1]