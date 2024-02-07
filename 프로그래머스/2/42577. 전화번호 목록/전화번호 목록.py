def solution(phone_book):
    answer = True
    d = {}
    for phone in phone_book:
        d[phone] = 1
    for phone in phone_book:
        temp = ""
        for num in phone:
            temp += num
            if temp in d and temp != phone:
                answer = False
        
    return answer