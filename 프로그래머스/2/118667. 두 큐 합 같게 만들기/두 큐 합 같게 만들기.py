from collections import deque

def solution(queue1, queue2):
    count = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
        
    while True:
        if sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
        elif sum1 < sum2:
            temp = queue2.popleft()
            queue1.append(temp)
            sum1 += temp
            sum2 -= temp
        else:
            break
        if (len(queue1)+len(queue2))*3 < count:
            return -1
        count += 1
        
    return count