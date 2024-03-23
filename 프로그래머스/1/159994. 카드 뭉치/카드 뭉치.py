def solution(cards1, cards2, goal):
    answer = "No"
    i, j, k = 0, 0, 0

    for word in goal :
        if i < len(cards1) and cards1[i] == word :
            i += 1
        elif j < len(cards2) and cards2[j] == word :
            j += 1
    
    if i + j == len(goal) :
        answer = "Yes"

    return answer