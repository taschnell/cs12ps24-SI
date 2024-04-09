"""
Dice Loop
"""
import random

line = 0

print("Press Enter to Role!")
while True:
    
    intake = input()
    if intake =="EXIT":
        break
    
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    
    # Dice 1
    match dice_1:
        case 1:
            print("\u2680")
        case 2:
            print("\u2681")
        case 3:
            print("\u2682")
        case 4:
            print("\u2683")
        case 5:
            print("\u2684")
        case 6:
            print("\u2685")

    # Dice 2
    match dice_2:
        case 1:
            print("\u2680")
        case 2:
            print("\u2681")
        case 3:
            print("\u2682")
        case 4:
            print("\u2683")
        case 5:
            print("\u2684")
        case 6:
            print("\u2685")

    print(f"Role Again? Type EXIT to stop")


print("Adios")