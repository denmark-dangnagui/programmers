s = input()
#K1KA5CB7
strings = []
numbers = []
for i in range(len(s)):
    if s[i].isalpha():
        strings.append(s[i])
    else:
        numbers.append(int(s[i]))

print(strings)
print(numbers)
print(sorted(strings))
print(sum(numbers))

#AJKDLSI421K4JSJ9D