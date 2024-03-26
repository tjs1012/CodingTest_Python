# skip에 포함된 알파벳을 제외하고 리스트에 저장함. / s의 각 문자 + index를 진행한 알파벳을 answer에 추가
import string
alphabet = list(string.ascii_lowercase)

def solution(s, skip, index) :
    answer = ''

    for i in skip :
        alphabet.remove(i)
    
    for string in s :
        num = (alphabet.index(string) + index) % len(alphabet)
        answer += alphabet[num]
    return answer