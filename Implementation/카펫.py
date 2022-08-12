def solution(brown, yellow):
    total = brown + yellow
    y = []
    for i in range(1, total + 1):
        if total % i == 0:
            y.append(i)
    for i in y:
        temp = total // i
        if i >= temp and (i-2) * (temp - 2) == yellow:
            return (i,temp)