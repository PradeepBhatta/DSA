def binary_search(value, arr):
    ub = len(arr) - 1
    lb = 0
    found = False
    while found == False and lb <= ub:
        mid = (lb + ub) // 2
        if arr[mid] == value:
            found = True
        elif arr[mid] > value:
            ub = mid - 1
        else:
            lb = mid + 1

    return found


def verify(result):
    if result:
        print("Data Found !!!")
    else:
        print("Error 404")


def insertion_sort(arr):
    for i in range(1, len(arr)):
        item_insert = arr[i]
        current_item = i - 1
        while arr[current_item] > item_insert and current_item > -1:
            arr[current_item + 1] = arr[current_item]
            current_item = current_item - 1
        arr[current_item + 1] = item_insert

    return arr


lst = [2, 4, 7, 98, 46, 3, 0, 33, 67]
lst = (insertion_sort(lst))
print(lst)

val = int(input("Enter a number to search "))
verify(binary_search(val, lst))
