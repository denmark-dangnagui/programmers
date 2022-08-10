def solution(answers):
    a = [1,2,3,4,5] * 10000
    b = [2,1,2,3,2,4,2,5] * 10000
    c = [3,3,1,1,2,2,4,4,5,5] * 10000
    score = []
    p_a,p_b,p_c =0,0,0
    for i in range(len(answers)):
        if a[i] == answers[i]:
            p_a += 1
        if b[i] == answers[i]:
            p_b += 1
        if c[i] == answers[i]:
            p_c += 1
    score.append(p_a)
    score.append(p_b)
    score.append(p_c)
    result = list(filter(lambda x: score[x] == max(score), range(len(score))))
    e = []
    for i in result:
        e.append(i+1)
    return e