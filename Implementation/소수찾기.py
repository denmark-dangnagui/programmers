from itertools import permutations
import math
def solution(numbers):
    c = []
    l = []
    answer = []
    for j in range(len(numbers)+1):
        for i in permutations(numbers,j):
            c.append(list(i))
    for i in c:
        l.append(''.join(i))
    for i in range(1,len(l)):
        answer.append(int(l[i]))
    answer = list(set(answer))
    answer.sort()
    result = 0
    for i in answer:
        cnt = 0
        if i > 1:
            for j in range(2,int(math.sqrt(i)) + 1):
                if i % j == 0:
                    cnt += 1
            if cnt == 0:
                result += 1
    return (result)