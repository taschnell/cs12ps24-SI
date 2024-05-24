import sys

intake_list = list(sys.stdin.readlines())

intake = iter(intake_list)
line_count = 0

mean = 0
intake_sum = 0
num_list = []
while True:
    try:
        line = next(intake)
        line_num = int((line.split())[2])
        line_count += 1
        intake_sum += line_num
        num_list.append(line_num)
        


    except StopIteration:
        break

mean = intake_sum/line_count
minimum = min(num_list)
maximum = max(num_list)
min_index = num_list.index(minimum)
max_index = num_list.index(maximum)

print(mean)
print(intake_list[max_index], intake_list[min_index])

