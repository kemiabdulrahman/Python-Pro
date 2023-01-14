import re

# File name
file_name = "note.txt"

# Open the file and read its contents
with open(file_name, "r") as file:
    text = file.read()

# Split the text into sentences
sentences = re.split(r"(?<=[.!?])\s+", text)

# Create a list to store the questions
questions = []

# Create a question for each sentence
for sentence in sentences:
    question = " ".join(sentence.split()[1:]) + "?"
    questions.append(question)

# Print the questions
for question in questions:
    print(question)

