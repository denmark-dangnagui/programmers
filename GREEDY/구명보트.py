def solution(people, limit):
    cnt = 0

    people.sort()
    print(people)

    start, end = 0, len(people) - 1
    while start <= end:
        cnt += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return (cnt)