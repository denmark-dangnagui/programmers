from collections import deque
def solution(progresses, speeds):
    p = deque(progresses)
    s = deque(speeds)
    result = []
    r = []
    while len(p) != 0:
        cnt = 0
        for i in range(len(p)):
            if p[i] >= 100:
                continue
            else:
                p[i] += s[i]
        while p:
            if p[0] >= 100:
                cnt += 1
                p.popleft()
                s.popleft()
            else:
                break
        result.append(cnt)
    for i in result:
        if i != 0:
            r.append(i)
    return r