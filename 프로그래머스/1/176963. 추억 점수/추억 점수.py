# name에 있는지 하나씩 확인하면서 점수 계산(딕셔너리 활용)
def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    for i in photo :
        score = 0
        for j in i :
            if j in dic :
                score += dic[j]
        answer.append(score)

    return answer