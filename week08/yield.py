# Creating a generator expression to generate squares of numbers from 1 to 5

def gen_test():
    
    y = (x**2 for x in range(1, 6))


    yield next(y)

while True:
    input()

    print(gen_test())