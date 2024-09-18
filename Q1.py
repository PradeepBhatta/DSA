ex = [2200, 2350, 2600, 2130, 2190]

print("Money spent extra in Feb than Jan = ", ex[1] -ex[0])

print("Expenses in first three months = ",ex[0]+ex[1]+ex[2])

if 2000 in ex :
    print("True")
else:
    print("False")

ex.append(1980)

ex[3] = ex[3] - 200

print(ex)