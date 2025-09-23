# List Comprehension Examples for All Data Types

# 1. Numbers (int / float)
print("Numbers:")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

halves = [x/2 for x in range(1, 6)]
print("Halves:", halves)

# 2. Strings
print("\nStrings:")
words = ['apple', 'banana', 'cherry']
upper_words = [word.upper() for word in words]
print("Uppercase:", upper_words)

first_letters = [word[0] for word in words]
print("First letters:", first_letters)

# 3. Booleans
print("\nBooleans:")
numbers = [1, 2, 3, 4, 5]
is_even = [x % 2 == 0 for x in numbers]
print("Is even:", is_even)

# 4. Lists (nested lists)
print("\nNested Lists:")
matrix = [[1,2], [3,4], [5,6]]
flat = [num for row in matrix for num in row]
print("Flattened:", flat)

# 5. Dictionaries
print("\nDictionaries:")
d = {'a': 1, 'b': 2, 'c': 3}
doubled_values = {k: v*2 for k, v in d.items()}
print("Doubled values:", doubled_values)

# 6. Sets
print("\nSets:")
nums = {1, 2, 3, 4}
squares_set = {x**2 for x in nums}
print("Squares set:", squares_set)

# 7. Tuples
print("\nTuples:")
tuple_list = [(x, x**2) for x in range(1, 4)]
print("Number, Square tuples:", tuple_list)

# 8. Conditional List Comprehension
print("\nConditional List Comprehension:")
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print("Even squares:", even_squares)
