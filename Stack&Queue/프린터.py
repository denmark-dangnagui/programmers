from collections import deque
def solution(priorities, location):
    p = deque(priorities)
    l = location + 1
    a = []
    cnt = 0
    while p:
        cnt += 1
        l -= 1
        if p[0] == max(p):
            a.append(p.popleft())
            if l == 0:
                return len(a)
        else:
            p.append(p.popleft())
            if l == 0:
                l = len(p)