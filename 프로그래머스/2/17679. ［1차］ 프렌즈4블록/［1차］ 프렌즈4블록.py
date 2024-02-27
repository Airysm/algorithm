def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    
    while True:
        temp = [[0 for _ in range(n)] for _ in range(m)]
        flag = True
        
        # 4개 블록 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0' and \
                    board[i][j] == board[i+1][j] and \
                    board[i][j] == board[i][j+1] and \
                    board[i][j] == board[i+1][j+1]:
                    temp[i][j], temp[i+1][j], temp[i][j+1], temp[i+1][j+1] = 1, 1, 1, 1
                    flag = False
        if flag:
            break
            
        # 4개 블록 점수 얻고 지우기
        for i in range(m):
            for j in range(n):
                if temp[i][j] == 1:
                    board[i][j] = '0'
                answer += temp[i][j]
        
        # 빈 공간에 블록 채우기
        while True:
            flag = True
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] != '0' and board[i+1][j] == '0':
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        flag = False
            if flag:
                break
                
    return answer