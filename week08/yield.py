# Creating a generator expression to generate squares of numbers from 1 to 5
squared_numbers = (x**2 for x in range(1, 6))
# Iterating over the generator expression and printing the squares
for num in squared_numbers:
    print(num)
