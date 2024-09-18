def recursive_binary_search(list, target):
    if len(list) == 0:
        return False

    midpoint = len(list) // 2 

    if list[midpoint] == target:
        return True
    elif list[midpoint] < target:
        return recursive_binary_search(list[midpoint + 1:], target) 
    else:
        return recursive_binary_search(list[:midpoint + 1], target) 


def verify(value):
    print(f"Target found: {value}")


lst = [i for i in range(1, 11) ]
result = recursive_binary_search(lst, 10)
verify(result)

a = []
result = recursive_binary_search(a, 10)
verify(result)