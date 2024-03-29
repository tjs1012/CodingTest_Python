def solution(data, ext, val_ext, sort_by) :
    answer = []

    standard = ["code", "date", "maximum", "remain"]
    a = standard.index(ext)
    
    for i in range(len(data)) :
        if data[i][a] < val_ext :
            answer.append(data[i])

    answer.sort(key = lambda x : x[standard.index(sort_by)])
    return answer