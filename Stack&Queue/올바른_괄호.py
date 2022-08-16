def solution(s):
    s = list(s)
    stack = []
    while s:
        if not stack:
            stack.append(s.pop())
        else:
            if s[-1] == ')':
                stack.append(s.pop())
            elif s[-1] == '(':
                if stack[-1] == ')':
                    s.pop()
                    stack.pop()
                elif stack[-1] == '(':
                    stack.append(s.pop())
    if not stack:
        return True
    else:
        return False