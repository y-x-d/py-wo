def mysum(*args, x = 0):
    sum = 0
    for number in args:
        sum += number

    return(sum + x)

print(mysum(1, 2, 3))
print(mysum(*[1, 2, 3]))
print(mysum(10, 20, 30, 40, 50))
print(mysum())

# print(mysum((2, 3, 4), 5))
# print(mysum((2, 3, 4), 0))

