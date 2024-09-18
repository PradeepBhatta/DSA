
def bubble_sort(arr):
    swap = True
    while swap == True and len(arr) > 0:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap = True


lst = [2, 4, 7, 98, 46, 3, 0, 33, 67]
print(lst)
bubble_sort(lst)
print(lst)
