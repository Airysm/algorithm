def solution(sequence):
    num_max = 0
    num = 0
    pulse = 1
    
    for n in sequence:
        n *= pulse
        pulse *= -1
        num += n
        num_max = max(num_max, num)
        if num < 0:
            num = 0
    num = 0
    pulse = -1
    for n in sequence:
        n *= pulse
        pulse *= -1
        num += n
        num_max = max(num_max, num)
        if num < 0:
            num = 0
    return num_max