# Chapter 4 - Exercise Solutions

# The contact book project already demonstrates all key concepts.
# Additional exercises:

# 1. List comprehension: even squares
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print("Even squares:", even_squares)

# 2. Dictionary: word frequency counter
text = "the cat sat on the mat the cat"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Frequencies:", freq)

# 3. Set operations
python_students = {"Alice", "Bob", "Charlie", "Diana"}
ai_students = {"Charlie", "Diana", "Eve", "Frank"}
print("Both:", python_students & ai_students)
print("Either:", python_students | ai_students)
print("Python only:", python_students - ai_students)
