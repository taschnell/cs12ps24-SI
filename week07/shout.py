import sys

intake = iter(sys.stdin)


while True:
    try:
        line = next(intake)
        print(line.upper(), end="")
    except StopIteration:
        break
