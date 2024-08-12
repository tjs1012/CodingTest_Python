import math

def solution(n) :
    answer = 1
    cnt = 1
    while (n - 2 * cnt) >= 0 :
        answer += math.factorial(n - cnt) // (math.factorial(cnt) * math.factorial(n - 2 * cnt))
        cnt += 1
    
    answer = answer % 1234567
    return answer