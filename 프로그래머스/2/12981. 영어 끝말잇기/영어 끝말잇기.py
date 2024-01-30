def solution(n, words):
    words_d = dict()
    order = 0
    temp = words[0][0]
    for word in words:
        if word[0] != temp or word in words_d:
            break
        words_d[word] = 0
        order += 1
        temp = word[-1]
        
    answer = [0, 0] if len(words) == order else [order%n+1, int(order/n)+1]
    return answer