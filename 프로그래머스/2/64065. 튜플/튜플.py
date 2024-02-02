def solution(s):
    answer = []
    l = []
    
    for set in s.split("},"):
        l.append(set.replace("{","").replace("}","").split(","))
    l.sort(key=len)
    
    for i in l:
        for j in i:
            j = int(j)
            if j not in answer: answer.append(j)
    
    # 조합해서 출력
    return answer