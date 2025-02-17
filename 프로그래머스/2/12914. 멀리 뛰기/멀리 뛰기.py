def solution(n):
    if n < 3:
        return n
    d = [0] * (n + 1)
    d[1], d[2] = 1, 2
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[-1]%1234567