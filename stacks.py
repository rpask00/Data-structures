# Python program to
# demonstrate stack implementation
# using collections.deque


from collections import deque


def valid_expression(exp):
    stack = deque()
    open_brackets = ['(', '[', '<']
    close_brackets = [')', ']', '>']

    for e in exp:
        if e in open_brackets:
            stack.append(e)

        if e in close_brackets:
            if e == '>':
                if stack.pop() != '<':
                    return False
            if e == ')':
                if stack.pop() != '(':
                    return False
            if e == ']':
                if stack.pop() != '[':
                    return False
    try:
        stack.pop()
        return False
    except:
        return True


print(valid_expression('((1+[2-3]-<4>+17)'))
