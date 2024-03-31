# 숫자로 변환해서 계산
def solution(today, terms, privacies) :
    answer = []
    today = int(today.replace(".", ""))
    dic = dict()
    for i in range(len(terms)) :
        dic[terms[i][0]] = int(terms[i][2:])

    for i in range(len(privacies)) :
        num = int(privacies[i][:10].replace(".", "")) + (dic[privacies[i][-1]] // 12) * 10000 + (dic[privacies[i][-1]] % 12) * 100 - 1
        if str(num)[-2:] == '00' :
            num = num - 100 + 28
        if int(str(num)[4:6]) > 12 : 
            num = num + 10000 - 1200
        if num < today : 
            answer.append(i + 1)

    return answer