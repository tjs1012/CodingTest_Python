def solution(keymap, targets) :
    answer = []
    
    dic = dict() # 각 문자에 대한 인덱스 정보를 저장하고 있는 dictionary
    for i in keymap :
        for index, string in enumerate(i) :
            if string in dic and (index + 1) > dic[string] : # 이미 해당 문자가 존재하고 인덱스 값도 크면 pass
                pass
            else : 
                dic[string] = index + 1

    for i in targets :
        count = 0
        for string in i :
            if string in dic :
                count += dic[string]
            else :
                count = -1
                break
        answer.append(count)
    
    return answer