def solution(brown, yellow):
    area = brown + yellow
    
    for i in range(1, area):
         if area % i == 0:
                b = int(i * 2 + (area / i) * 2 - 4)
                y = int(area - b)
                if brown == b and yellow == y:
                    answer = [int(area / i),i]
                    break
                    
    return answer