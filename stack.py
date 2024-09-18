stack = [None]*10
print(stack)
tos = -1


def push(item):
    global tos
    if tos < len(stack)-1:
        tos = tos + 1
        stack[tos] = item
    else:
        print("Stack is full")


def pop():
    global tos
    if tos == -1:
        print("Stack is empty")
    else:
        stack[tos] = None
        tos = tos-1


push(10)
push(000)
print(stack)
pop()
pop()
pop()
push(1)


print(stack)


