"""
Infinite Input
"""


line = 0
all_input = ""
intake = ""
while intake != "EXIT": 
    print(f"Please some input on line {line}? Type EXIT to quit!")
    
    all_input = all_input + intake
    line = line + 1
    intake = input()


print("Adios\nYOUR INPUT: ", all_input)