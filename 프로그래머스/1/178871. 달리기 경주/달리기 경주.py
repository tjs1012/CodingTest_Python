def solution(players, callings) :
    answer = []
    players_dic = {player : index for index, player in enumerate(players)}

    for i in callings :
        num = players_dic[i]
        players_dic[players[num - 1]] += 1
        players_dic[i] -= 1
        players[num - 1], players[num] = players[num], players[num - 1]

    answer = players

    return answer