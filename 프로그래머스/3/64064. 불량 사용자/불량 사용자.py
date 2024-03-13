from collections import defaultdict

def check_id(user, banned):
    if len(user) != len(banned):
        return False
    for i in range(len(user)):
        if user[i] != banned[i] and banned[i] != '*':
            return False
    return True

def solution(user_id, banned_id):
    answer = set()
    visited = [False for _ in range(len(user_id))]

    def dfs(depth):
        if depth == len(banned_id):
            temp = []
            for i in range(len(visited)):
                if visited[i]:
                    temp.append(user_id[i])
            answer.add(tuple(temp))
            return
        
        for i in range(len(user_id)):
            if not visited[i] and check_id(user_id[i], banned_id[depth]):
                visited[i] = True
                dfs(depth+1)
                visited[i] = False
    dfs(0)
    return len(answer)