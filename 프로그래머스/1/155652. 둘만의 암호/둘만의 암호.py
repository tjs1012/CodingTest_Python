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