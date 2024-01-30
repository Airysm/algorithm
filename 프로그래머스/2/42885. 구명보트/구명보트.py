from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    d = deque(people)
    answer = 0
    
    while d:
        if len(d) == 1:
            d.pop()
        elif d[0] + d[-1] <= limit:
            d.pop()
            d.popleft()
        else:
            d.popleft()
        answer += 1
        
    return answer