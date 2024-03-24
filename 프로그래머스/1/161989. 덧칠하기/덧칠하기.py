def solution(n, m, section):
    answer = 1
    num = section[0]
    for i in range(1, len(section)) :
        if num < section[i] < num + m :
            pass
        else :
            answer += 1
            num = section[i]
    return answer