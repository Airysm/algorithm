import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def div_card(arrayA, arrayB):
    gcd_a = arrayA[0]
    
    for a in arrayA:
        gcd_a = gcd(a, gcd_a)
    for b in arrayB:
        if b%gcd_a == 0:
            return 0
    return gcd_a

def solution(arrayA, arrayB):
    return max(div_card(arrayA, arrayB), div_card(arrayB, arrayA))