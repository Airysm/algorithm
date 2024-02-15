def solution(word):
    answer = 0
    alphabet = "AEIOU"
    num_list = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += num_list[i] * alphabet.find(word[i])
        answer += 1
                
    return answer