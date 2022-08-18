from collections import deque

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
p = deque(progresses)
s = deque(speeds)
result = []
qwe = 0
while len(p) != 0:
    qwe += 1
    cnt = 0
    for i in range(len(p)):
        if p[i] == 100:
            continue
        else:
            p[i] += s[i]
    while p:
        if p[0] == 100:
            cnt += 1
            p.popleft()
            s.popleft()
        else:
            break
    result.append(cnt)

print(result)