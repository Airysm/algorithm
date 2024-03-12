def max_sequence(sequence, pulse):
    num_max = 0
    num = 0
    
    for n in sequence:
        n *= pulse
        pulse *= -1
        num += n
        num_max = max(num_max, num)
        if num < 0:
            num = 0
            
    return num_max

def solution(sequence):
    return max(max_sequence(sequence, 1), max_sequence(sequence, -1))