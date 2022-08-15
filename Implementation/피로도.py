from  itertools import permutations
def solution(k, dungeons):
    npr = list(permutations(dungeons))
    result = 0
    for i in npr:
        hp = k
        cnt = 0
        for j in i:
            if hp < j[0]:
                break
            hp -= j[1]
            cnt += 1
        if cnt > result:
            result = cnt
    return(result)