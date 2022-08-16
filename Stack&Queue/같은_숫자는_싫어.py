def solution(arr):
    stack = []
    result = []
    while arr:
        if not stack:
            stack.append(arr.pop())
        if arr and stack[-1] == arr[-1]:
            arr.pop()
        elif arr and stack[-1] != arr[-1]:
            stack.append(arr.pop())
    return(stack[::-1])