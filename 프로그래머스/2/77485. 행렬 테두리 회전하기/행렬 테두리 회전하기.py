def solution(rows, columns, queries):
    answer = []
    matrix = [ 
        [0 for i in range(columns)]
        for j in range(rows)
    ]
    
    t = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = t
            t += 1
            
    for q in queries:
        for i in range(len(q)):
            q[i] -= 1
            
        min_num = rows*columns
        temp = matrix[q[0]][q[1]]
        
        for i in range(q[0], q[2]):
            t = matrix[i+1][q[1]]
            matrix[i][q[1]] = t
            min_num = min(min_num, t)
        for i in range(q[1], q[3]):
            t = matrix[q[2]][i+1]
            matrix[q[2]][i] = t
            min_num = min(min_num, t)
        for i in range(q[2], q[0], -1):
            t = matrix[i-1][q[3]]
            matrix[i][q[3]] = t
            min_num = min(min_num, t)
        for i in range(q[3], q[1], -1):
            t = matrix[q[0]][i-1]
            matrix[q[0]][i] = t
            min_num = min(min_num, t)
            
        min_num = min(min_num, temp)
        matrix[q[0]][q[1]+1] = temp
        
        answer.append(min_num)
        
    return answer