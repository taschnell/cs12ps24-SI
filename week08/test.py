x = [ 1,12,3,4,4,5,5]


1 #TRUE
0 #FALSE

for num in x:
    if num % 2:
        print(num)

gen = (print(num) for num in x if num % 2)

