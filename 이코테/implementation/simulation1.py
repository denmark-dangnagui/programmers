n = int(input())
movement = list(map(str,input().split()))
location = [1,1]
for i in movement:
    if i == 'R':
        if location[1] + 1 <= n:
            location[1] += 1
    elif i == 'L':
        if location[1] - 1 > 0:
            location[1] -= 1
    elif i == 'U':
        if location[0] - 1 > 0:
            location[0] -= 1
    elif i == 'D':
        if location[0] + 1 <= n:
            location[0] += 1
print(location)