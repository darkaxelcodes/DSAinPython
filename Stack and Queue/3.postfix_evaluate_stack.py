from Stack import MyStack

def evaluate_post_fix(exp):
    stack = MyStack()
    for i in exp:
        if i.isdigit():
            stack.push(i)
        else:
            right = stack.pop()
            left = stack.pop()
            stack.push(str(eval(left + i + right)))
    return int(float(stack.peek()))


