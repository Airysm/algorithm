from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_num = dict(zip(want, number))
    
    for i in range(len(discount) - 9):
        if want_num == Counter(discount[i:i+10]):
            answer += 1
    return answer