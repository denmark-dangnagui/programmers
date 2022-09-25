def sol(n, q):
    answer = []
    ip = [0] * n
    temp = []
    m = {}
    for i in q:
        temp.append(i.split())
    for i in temp:
        print()
        print('ip : ', ip)
        if i[1] == 'request':
            if 0 in ip:
                if i[0][7] not in m :
                    idx = ip.index(0)
                    m[i[0][7]] = idx + 1
                    ip[idx] = 1
                    print(idx)
                    print(ip)
                    print(m)
                    print(i[0][7])
                    num = float(m[i[0][7]]) * 0.1
                    print(num)
                    print()
                    answer.append(i[0]+' 172.90.' +''+ str(num))
                else:
                    print('여기 들어왕ㅆ땅')
                    e = ip.index(0)
                    print(e)
                    print(m[i[0][7]])
                    m[i[0][7]] = e + 1
                    print('ewjoefwoij', m[i[0][7]])
                    ip[e] = 1
                    print(ip)
                    num = float(m[i[0][7]]) * 0.1
                    answer.append(i[0] + ' 172.90.' + '' + str(num))

            else:
                print('reject')
                answer.append(i[0]+' reject')
        elif i[1] == 'release':
            # print(int(i[0][7]))
            ip[int(i[0][7]) - 1] = 0
            print(ip)
            print('rel',ip)
    return answer


q = ['desktop2 request','desktop1 request','desktop3 request', 'desktop2 release','desktop1 release','desktop3 request','desktop2 request','desktop3 release','desktop2 release','desktop2 request']
answer = sol(2,q)
print(answer)