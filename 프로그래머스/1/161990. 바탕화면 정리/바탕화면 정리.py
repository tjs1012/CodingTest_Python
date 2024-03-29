# 좌표 기준 0번 인덱스 중 (가장 작은 수)와 1번 인덱스 중 (가장 작은 수), 0번 인덱스 중 (가장 큰 수 + 1), 1번 인덱스 중 (가장 큰 수 + 1) 추가
def solution(wallpaper) :
    answer = []

    lst = []
    for i in range(len(wallpaper)) :
        temp = [i]
        if '#' in wallpaper[i] :
            for j in range(len(wallpaper[i])) :
                if '#' == wallpaper[i][j] :
                    temp.append(j)
                if len(temp) == 2 :
                    lst.append(temp)
                    temp = [i]

    answer.append(min(lst, key = lambda x : x[0])[0])
    answer.append(min(lst, key = lambda x : x[1])[1])
    answer.append(max(lst, key = lambda x : x[0])[0] + 1)
    answer.append(max(lst, key = lambda x : x[1])[1] + 1)
    return answer