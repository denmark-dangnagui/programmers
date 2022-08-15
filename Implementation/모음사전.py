def solution(word):
    w = ['A','E','I','O','U']
    words = []
    for a in w:
        words.append(a)
        for b in w:
            words.append(a+b)
            for c in w:
                words.append(a+b+c)
                for d in w:
                    words.append(a+b+c+d)
                    for e in w:
                        words.append(a+b+c+d+e)
    return(words.index(word)+1)