def solution(board, h, w) :
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4) :
        new_h = h + dy[i]
        new_w = w + dx[i]
        if 0 <= new_h < len(board) and 0 <= new_w < len(board[0]) :
            if board[new_h][new_w] == board[h][w] :
                answer += 1
    return answer