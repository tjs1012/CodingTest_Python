def solution(word) :
    answer = 0

    lst = ['A', 'E', 'I', 'O', 'U']
    num = [[1,782,1563,2344,3125], [1,157,313,469,625], [1,32,63,94,125], [1,7,13,19,25], [1,2,3,4,5]] # 각 자리별 규칙성

    for i in range(len(word)) :
        answer += num[i][lst.index(word[i])]

    return answer