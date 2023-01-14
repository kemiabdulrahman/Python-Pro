import random

# List of people's names
people = ["John", "Jane", "Bob", "Sara"]

# Generate a random number for each person
numbers = {}
for person in people:
    numbers[person] = random.randint(1, 10)

# Ask each person to answer a question pertaining to their number
scores = {}
for person in people:
    print(f"{person}, what is the square of the number {numbers[person]}?")
    answer = int(input())
    scores[person] = abs(answer - (numbers[person]**2))

# Sort the people by their score
sorted_people = sorted(scores.items(), key=lambda x: x[1])

# Print the ranking
print("Ranking:")
for i, (person, score) in enumerate(sorted_people):
    print(f"{i + 1}. {person} (score: {score})")

