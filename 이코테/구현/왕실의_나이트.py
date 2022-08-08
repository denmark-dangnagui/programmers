n = input()
cnt = 0
location = []
if n[0] == 'a':
    n = n.replace('a',str(1))
elif n[0] == 'b':
    n = n.replace('b',str(2))
elif n[0] == 'c':
    n = n.replace('c',str(3))
elif n[0] == 'd':
    n = n.replace('d',str(4))
elif n[0] == 'e':
    n = n.replace('e',str(5))
elif n[0] == 'f':
    n = n.replace('f',str(6))
elif n[0] == 'g':
    n = n.replace('g',str(7))
elif n[0] == 'h':
    n = n.replace('h',str(8))
location.append(int(n[0]))
location.append(int(n[1]))

if location[0] + 2 < 9:
    if location[1] + 1 < 9:
        cnt += 1
    if location[1] - 1 > 0:
        cnt += 1
if location[0] - 2 > 0:
    if location[1] + 1 < 9:
        cnt += 1
    if location[1] - 1 > 0:
        cnt += 1
if location[1] - 2 > 0:
    if location[0] + 1 < 9:
        cnt += 1
    if location[0] - 1 > 0:
        cnt += 1
if location[1] + 2 < 9:
    if location[0] + 1 < 9:
        cnt += 1
    if location[0] - 1 > 0:
        cnt += 1
print(cnt)