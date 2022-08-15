def solution(sizes):
    temp1 = []
    temp2 = []
    for i in sizes:
        temp1.append(max(i))
    for i in sizes:
        temp2.append(min(i))
    result = max(temp1) * max(temp2)
    return(result)
