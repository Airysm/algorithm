def solution(msg):
    word = {}
    answer = []
    
    for i in range(26):
        word[chr(65+i)] = i + 1
    
    w1, w2 = 0, 0
    while True:
        w2 += 1
        if w2 == len(msg):
            answer.append(word[msg[w1:w2]])
            break
        if msg[w1:w2+1] not in word:
            word[msg[w1:w2+1]] = len(word) + 1
            answer.append(word[msg[w1:w2]])
            w1 = w2
            
    return answer