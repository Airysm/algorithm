def solution(routes):
    answer = 0
    camera = -30000
    
    routes.sort(key=lambda x:x[1])
    print(routes)
    for route in routes:
        if camera < route[0]:
            print(route[0])
            answer += 1
            camera = route[1]
            
    return answer