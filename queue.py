queue = [None] * 10
headP = 0
tailP = -1
NoOfItems = 0


def enqueue(item):
    global NoOfItems, tailP
    if NoOfItems >= len(queue):
        print("Queue is full")
    else:
        tailP = tailP + 1
        if tailP > 9:
            tailP = 0
        queue[tailP] = item
        NoOfItems += 1


def dequeue():
    global NoOfItems, headP
    if NoOfItems > 0:
        item = queue[headP]
        queue[headP] = None
        NoOfItems -= 1
        if NoOfItems == 0:
            headP = -1
        else:
            headP = headP + 1
            if headP > 9:
                headP = 0
    else:
        print("Queue is empty")
    return item


for i in range(9):
    enqueue(i * i)

print(queue)
print(dequeue())
print(dequeue())
print(dequeue())
print(queue)

