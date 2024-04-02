# S의 위치를 찾아 입력된 명령대로 이동
def solution(park, routes) :
    answer = []
    H = len(park) - 1
    W = len(park[0]) - 1

    for i in range(len(park)) :
        if 'S' in park[i] :
            answer.append(i)
            answer.append(park[i].index('S'))
            break

    for j in range(len(routes)) : # 현재 위치에서 이동되는 위치까지 X가 없는지 확인
        if routes[j][0] == 'N' and answer[0] - int(routes[j][2:]) >= 0 :
            for k in range(1, int(routes[j][2:]) + 1) :
                if park[answer[0] - k][answer[1]] == 'X' :
                    break
                else :
                    if k == int(routes[j][2:]) :
                        answer[0] = answer[0] - int(routes[j][2:])
        
        if routes[j][0] == 'S' and answer[0] + int(routes[j][2:]) <= H :
            for k in range(1, int(routes[j][2:]) + 1) :
                if park[answer[0] + k][answer[1]] == 'X' :
                    break
                else :
                    if k == int(routes[j][2:]) :
                        answer[0] = answer[0] + int(routes[j][2:])
        
        if routes[j][0] == 'W' and answer[1] - int(routes[j][2:]) >= 0 :
            for k in range(1, int(routes[j][2:]) + 1) :
                if park[answer[0]][answer[1] - k] == 'X' :
                    break
                else :
                    if k == int(routes[j][2:]) :
                        answer[1] = answer[1] - int(routes[j][2:])

        if routes[j][0] == 'E' and answer[1] + int(routes[j][2:]) <= W :
            for k in range(1, int(routes[j][2:]) + 1) :
                if park[answer[0]][answer[1] + k] == 'X' :
                    break
                else :
                    if k == int(routes[j][2:]) :
                        answer[1] = answer[1] + int(routes[j][2:])

    return answer