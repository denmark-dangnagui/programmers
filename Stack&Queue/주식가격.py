from collections import deque
def solution(prices):
    answer = []
    p = deque(prices)
    while p:
        sec = 0
        for j in range(len(p)-1):
            sec += 1
            if p[0] > p[j+1]:
                break
        p.popleft()
        answer.append(sec)
    return answer