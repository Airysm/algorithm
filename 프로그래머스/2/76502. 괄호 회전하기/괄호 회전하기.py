def parenthesis_correct(s):
    stack = []
    for c in s:
        if stack:
            if c == ')' and stack[-1] == '(':   stack.pop()
            elif c == '}' and stack[-1] == '{': stack.pop()
            elif c == ']' and stack[-1] == '[': stack.pop()
            else:   stack.append(c)
        else:
            stack.append(c)
    return False if stack else True

def solution(s):
    x = 0
    
    for i in range(len(s)):
        if parenthesis_correct(s): x += 1
        s = s[1:] + s[0]
    # 회전하면서 확인
    return x