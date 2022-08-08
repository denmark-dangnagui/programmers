def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    a_lost = list(lost.difference(reserve))
    a_reserve = list(reserve.difference(lost))
    cnt = n
    cnt -= len(a_lost)
    for i in a_lost:
        if i-1 in a_reserve:
            cnt += 1
            a_reserve.remove(i-1)
        elif i+1 in a_reserve:
            cnt += 1
            a_reserve.remove(i+1)
    return cnt