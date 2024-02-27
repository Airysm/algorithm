def solution(files):
    answer = []
    temp = []
    
    for file in files:
        head, number = "", ""
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                break
        for j in range(len(number)):
            if not number[j].isdigit():
                number = number[:j]
                break
        temp.append([head, number, file])
    
    temp = sorted(temp, key=lambda x:(x[0].lower(), int(x[1])))
    
    for t in temp:
        answer.append(t[2])
        
    return answer