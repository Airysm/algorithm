def n_base(num, n):
    base_char = "0123456789ABCDEF"
    result = ''
    if num == 0:
        return '0'
    while num > 0:
        result += base_char[num % n] 
        num //= n
    
    return result[::-1]

def solution(n, t, m, p):
    all_num = ''
    i = 0
    while len(all_num) <= p - 1 + (t-1) * m:
        all_num += n_base(i, n)
        i += 1
    all_num = all_num[:p+(t-1)*m]
    
    return all_num[p-1::m]