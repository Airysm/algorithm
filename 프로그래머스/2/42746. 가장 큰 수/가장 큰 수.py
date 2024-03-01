def solution(numbers):
    answer = ''
    
    strnum = list(map(str, numbers))
    strnum.sort(key=lambda x:x*3, reverse=True)
        
    return str(int(''.join(strnum)))