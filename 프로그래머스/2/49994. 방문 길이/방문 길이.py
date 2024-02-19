def solution(dirs): 
    x, y = 0, 0
    record = set()
    for c in dirs:
        if c == 'U' and y < 5:
            record.add(((x, y), (x, y+1)))
            y += 1
        elif c == 'D' and y > -5:
            record.add(((x, y-1), (x, y)))
            y -= 1
        elif c == 'R' and x < 5:
            record.add(((x, y), (x+1, y)))
            x += 1
        elif c == 'L' and x > -5:
            record.add(((x-1, y), (x, y)))
            x -= 1
    return len(record)