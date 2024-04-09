# Take input from the user
user_input = input("Enter a line of text: ")

# Split the input line into words
words = user_input.split()

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words back into a line
sorted_line = ' '.join(sorted_words)

# Print the sorted line
print("Sorted line:", sorted_line)
