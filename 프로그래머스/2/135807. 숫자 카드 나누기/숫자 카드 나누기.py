import math

def div_card(arrayA, arrayB):
    arrayA.sort()
    cdA = []
    
    for i in range(1, int(math.sqrt(arrayA[0]))):
        if arrayA[0]%i == 0:
            if i > 1:
                cdA.append(i)
            cdA.append(arrayA[0]//i)

    cdA.sort(reverse=True)
    
    for i in cdA:
        flag = True
        for a in arrayA:
            if a%i != 0:
                flag = False
                break
        for b in arrayB:
            if b%i == 0:
                flag = False
                break
        if flag:
            return i
    return 0

def solution(arrayA, arrayB):
    return max(div_card(arrayA, arrayB), div_card(arrayB, arrayA))