def solution(x, y, n):
    dp = [1e8 for _ in range(y+1)]
    dp[x] = 0
    
    for v in range(x, y+1):
        if v + n <= y:
            dp[v+n] = min(dp[v+n], dp[v] + 1)
        if v * 2 <= y:
            dp[v*2] = min(dp[v*2], dp[v] + 1)
        if v * 3 <= y:
            dp[v*3] = min(dp[v*3], dp[v] + 1)
    
    return dp[y] if dp[y] < 1e8 else -1