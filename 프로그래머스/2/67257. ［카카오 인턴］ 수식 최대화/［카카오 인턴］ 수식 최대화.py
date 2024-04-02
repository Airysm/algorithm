from collections import deque
                
def calculate(expression, op):
    arr_exp = deque()
    temp = ""
    for e in expression:
        if e.isdigit() == True:
            temp += e
        else:
            arr_exp.append(temp)
            arr_exp.append(e)
            temp = ""
    arr_exp.append(temp)
    
    for o in op:
        stack = []
        while len(arr_exp) > 0:
            temp = arr_exp.popleft()
            if temp == o:
                stack.append(str(eval(stack.pop()+o+arr_exp.popleft())))
            else:
                stack.append(temp)
        arr_exp = deque(stack)
        
    return arr_exp[0]

def solution(expression):
    max_num = 0
    op_list = []
    
    def combi(n, order):
        if n == 3:
            op_list.append(order[:])
            return

        for o in ['*', '+', '-']:
            if o not in order:
                order.append(o)
                combi(n+1, order)
                order.pop()
    
    combi(0, [])
    
    for op in op_list:
        max_num = max(max_num, abs(int(calculate(expression, op))))
    
    return max_num