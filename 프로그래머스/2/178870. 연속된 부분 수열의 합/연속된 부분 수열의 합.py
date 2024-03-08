def solution(sequence, k):
    answer = []
    start = 0
    end = -1
    num = 0
    
    while True:
        if num < k:
            end += 1
            if end >= len(sequence):    break
            num += sequence[end]
        else:
            num -= sequence[start]
            if start >= len(sequence):  break
            start += 1
        if num == k:
                answer.append([start, end])
    
    answer.sort(key=lambda x:x[1]-x[0])
    return answer[0]