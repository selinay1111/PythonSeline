numbers = {1,2,3,4,5}

print({n for n in numbers if n > 3})

big_num = set()
for n in numbers:
    if n > 3:
        big_num.add(n)
print(big_num)

# 1. Create a list comprehension that returns the square of every number divisible by both 2 and 3.
numbers = [3, 8, 12, 15, 20, 25, 30]
print([n ** 2 for n in numbers if n % 2 == 0 and n % 3 == 0])

# 2. create a list of people who are at least 18 years old
names = ["Alice", "Bob", "Charlie", "David"]
ages = [17, 25, 30, 16]
print([name for (name, age) in zip(names, ages) if age >= 18])

# 3. Create a list comprehension that produces all combinations like "A1", "B2", etc., but only where the number is even.
letters = ["A", "B", "C"]
numbers = [1, 2, 3, 4]
# expected output: ['A2', 'A4', 'B2', 'B4', 'C2', 'C4']

# 4. Create a list comprehension that returns all words that:
# have more than 4 letters, and
# contain the letter "a".
words = ["apple", "banana", "pear", "kiwi", "orange", "plum"]

# 5. produce a list where if a student's score is 70 or above, give them a pass
students = [
    ("Alice", 85),
    ("Bob", 62),
    ("Charlie", 91),
    ("David", 48),
    ("Eva", 77)
]

# expected output: ["Alice: Pass", "Charlie: Pass", "Eva: Pass"]
