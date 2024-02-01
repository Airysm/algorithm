def solution(n, left, right):
    list = []
    
    for i in range(left, right+1):
        list.append(max(i//n, i%n) + 1)

    return list