def solution(word):
    alphabet = "AEIOU"
    num_list = []
    answer = 0
    num = 0
    
    for i in range(5):
        num += 5**i
        num_list.append(num)
    num_list = num_list[::-1]
    
    for i in range(len(word)):
        answer += num_list[i] * alphabet.find(word[i])
        answer += 1
                
    return answer