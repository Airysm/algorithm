def solution(s):
    zero = 0
    count = 0
    one = 0
    
    while not s == "1":
        zero += s.count('0')
        one = s.count('1')
        s = bin(one)[2:]
        count += 1
    
    return [count, zero]