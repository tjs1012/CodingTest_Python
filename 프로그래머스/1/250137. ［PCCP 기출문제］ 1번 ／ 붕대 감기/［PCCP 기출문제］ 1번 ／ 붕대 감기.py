# 매 시간대마다 체력 갱신
def solution(bandage, health, attacks) :
    answer = health
    cnt = 0
    sequence = 0
    for i in range(1, attacks[-1][0] + 1) :
        if i != attacks[cnt][0] : # 공격을 받지 않은 상황
            sequence += 1
            if sequence < bandage[0] :
                if answer + bandage[1] >= health :
                    answer = health
                else :
                    answer += bandage[1]
            elif sequence == bandage[0] :
                answer = answer + bandage[1] + bandage[2]
                sequence = 0
                if answer > health :
                    answer = health
        else : # 공격을 받은 상황
            answer -= attacks[cnt][1]
            sequence = 0
            cnt += 1
            if answer <= 0 :
                return -1
    return answer