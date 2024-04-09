my_dict = dict()


print("Please input a key value pair")

while True:
    try:
        intake = input().split()
        print(intake)
        my_dict[intake[0]] = intake[1]
    except EOFError:
        break

print(my_dict)