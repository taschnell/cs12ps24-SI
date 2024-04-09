pi = 3.141592653

# F-string rounding
print(f"Pi to 3 places: {pi:.3f}")

# cutting off all but the first 4 characters
print("Pi to 5 places: " + str(pi)[:5])

# Manually Rounding Pi
print("Rounded Pi: " + str(round(pi, 3)))


f_type = ".3f"

# Formatted Pi
print("Formatted Pi: " + format(pi, f_type))


