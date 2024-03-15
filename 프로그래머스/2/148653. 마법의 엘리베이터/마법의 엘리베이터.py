def solution(storey):
    count = 0
    
    while storey != 0:
        storey, mod = divmod(storey, 10)
        if mod == 5:
            if storey%10 > 4:
                storey += 1
            count += mod
        elif mod > 5:
            storey += 1
            count += 10 - mod
        else:
            count += mod
            
    return count