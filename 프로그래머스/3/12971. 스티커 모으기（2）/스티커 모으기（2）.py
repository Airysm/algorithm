def solution(sticker):
    answer = 0
    dp  = [0 for _ in range(len(sticker))]
    dp2 = [0 for _ in range(len(sticker))]
    
    if len(sticker) == 1:
        return sticker[0]
    
    dp[0] = sticker[0]
    dp[1] = max(sticker[0], sticker[1])
    for i in range(2, len(dp)-1):
        dp[i] = sticker[i]
        dp[i] = max(dp[i-2]+dp[i], dp[i-1])
    
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(dp)):
        dp2[i] = sticker[i]
        dp2[i] = max(dp2[i-2]+dp2[i], dp2[i-1])

    return max(dp[-2], dp2[-1])