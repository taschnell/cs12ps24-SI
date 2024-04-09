limit = 4000000
a, b = 1, 2
fib_sum = 0
while a <= limit:
    if a % 2 == 0:
        fib_sum += a
    temp = a + b
    a = b
    b = temp
    print(a)


print("Sum of even-valued terms in Fibonacci sequence up to {} is: {}".format(limit, fib_sum))
