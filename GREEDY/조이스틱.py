def solution(name):
    cnt = 0
    l_move = len(name) - 1
    for i, c in enumerate(name):
        cnt += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        next_ = i + 1
        while len(name) > next_ and name[next_] == 'A':
            next_ += 1
        move_l = (i * 2) + len(name) - next_
        move_r = (len(name) - next_) * 2 + i
        l_move = min(l_move, move_l, move_r)
    return (cnt + l_move)
