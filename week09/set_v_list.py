import time

def measure_time(data_structure, n):
    start_time = time.time()
    for i in range(n):
        _ = i in data_structure
    end_time = time.time()
    return end_time - start_time

n = 10000

my_list = list(range(n))

my_set = set(my_list)

list_time = measure_time(my_list, n)

set_time = measure_time(my_set, n)

# Output
print(f"Time taken for list membership check: {list_time} seconds")
print(f"Time taken for set membership check: {set_time} seconds")
print(f"Set is {list_time / set_time:.2f} times faster than list for membership check")
