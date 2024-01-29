def solution(s):
    answer = ""
    for i in range(len(s)):
        answer += s[i].upper() if i == 0 or s[i - 1] == ' ' else s[i].lower()
    return answer