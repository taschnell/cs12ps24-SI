# Example: Splitting a string into a list of words
my_string = "Hello, world! This is a split example."
words_list = my_string.split()
print("Split words:", words_list)

# Example: Splitting a string using a specific delimiter
my_string_with_delimiter = "apple,banana,orange,grape"
fruits_list = my_string_with_delimiter.split(",")
print("Split fruits:", fruits_list)

# Example: Splitting a string with a limit on the number of splits
sentence = "I like to eat apples, bananas, and oranges."
words_with_limit = sentence.split(" ", 4)
print("Split words with limit:", words_with_limit)
