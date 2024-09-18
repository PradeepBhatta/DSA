def linear_search(search):
    found = False
    index = 0
    while found == False and index < len(lst):
        if lst[index] == search:
            found = True
        index += 1
    return found


lst = [2, 4, 7, 98, 46, 3, 0, 33, 67]
val = int(input("Enter a number: "))
result = linear_search(val)
if result:
    print("Data Found !!!")
else:
    print("Error 404")
