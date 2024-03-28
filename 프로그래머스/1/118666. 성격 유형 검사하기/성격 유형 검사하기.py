def solution(survey, choices) :
    answer = ''
    list = [[0 for _ in range(2)] for _ in range(4)]
    score = [3, 2, 1, 0, 1, 2, 3]
    k = 0
    for i in survey :
        if 'RT' == i or 'TR' == i :
            if 'RT' == i and choices[k] <= 4 :
                list[0][0] += score[choices[k] - 1]
            elif 'RT' == i and choices[k] > 4 :
                list[0][1] += score[choices[k] - 1]
            elif 'TR' == i and choices[k] <= 4 :
                list[0][1] += score[choices[k] - 1]
            elif 'TR' == i and choices[k] > 4 :
                list[0][0] += score[choices[k] - 1]
        elif 'CF' == i or 'FC' == i :
            if 'CF' == i and choices[k] <= 4 :
                list[1][0] += score[choices[k] - 1]
            elif 'CF' == i and choices[k] > 4 : 
                list[1][1] += score[choices[k] - 1]
            elif 'FC' == i and choices[k] <= 4 :
                list[1][1] += score[choices[k] - 1]
            elif 'FC' == i and choices[k] > 4 :
                list[1][0] += score[choices[k] - 1]
        elif 'JM' == i or 'MJ' == i :
            if 'JM' == i and choices[k] <= 4 :
                list[2][0] += score[choices[k] - 1]
            elif 'JM' == i and choices[k] > 4 :
                list[2][1] += score[choices[k] - 1]
            elif 'MJ' == i and choices[k] <= 4 :
                list[2][1] += score[choices[k] - 1]
            elif 'MJ' == i and choices[k] > 4 :
                list[2][0] += score[choices[k] - 1]
        elif 'AN' == i or 'NA' == i :
            if 'AN' == i and choices[k] <= 4 :
                list[3][0] += score[choices[k] - 1]
            elif 'AN' == i and choices[k] > 4 :
                list[3][1] += score[choices[k] - 1]
            elif 'NA' == i and choices[k] <= 4 :
                list[3][1] += score[choices[k] - 1]
            elif 'NA' == i and choices[k] > 4 :
                list[3][0] += score[choices[k] - 1]
        k += 1
    print(list)
    
    if list[0][0] >= list[0][1] :
        answer += 'R'
    else :
        answer += 'T'
    if list[1][0] >= list[1][1] :
        answer += 'C'
    else :
        answer += 'F'
    if list[2][0] >= list[2][1] :
        answer += 'J'
    else :
        answer += 'M'
    if list[3][0] >= list[3][1] :
        answer += 'A'
    else :
        answer += 'N'

    return answer