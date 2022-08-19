from collections import deque
def solution(prices):
    answer = []
    p = deque(prices)
    t = len(p)
    while p:
        sec = 0
        print(p)
        for j in range(len(p)-1):
            print(1)
            if p[0] <= p[j+1]:
                sec += 1
        p.popleft()
        answer.append(sec)
    return answer