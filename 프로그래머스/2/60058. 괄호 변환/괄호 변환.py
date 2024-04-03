def make_correct_u(u, v):
    result = '('
    result += solution(v)
    result += ')'
    u = u[1:-1]
    for i in u:
        if i == '(':    result += ')'
        else:           result += '('
    return result

def check_correct_p(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True

def divide_p(p):
    count1 = 0
    count2 = 0
    for i in range(len(p)):
        if p[i] == '(':
            count1 += 1
        else:
            count2 += 1
        if count1 == count2:
            return p[:i+1], p[i+1:]

def make_correct_p(u):
    u, v = divide_p(u)
    if check_correct_p(u):
        return u + make_correct_p(v)
    else:
        return make_correct_u(u, v)

def solution(p):
    
    if len(p) == 0:
        return ''
    elif check_correct_p(p):
        return p
        
    return make_correct_p(p)