def create_stack():
    a = []
    return a


def is_empty(a):
    return len(stack) == 0


def push(a, num):
    a.append(num)
    print("Pushed number is " + num)


def pop(a):
    print("Popped number is " + a.pop())


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
pop(stack)
pop(stack)
