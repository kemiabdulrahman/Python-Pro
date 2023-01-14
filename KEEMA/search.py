import re

# File name
file_name = "textfile.txt"

# Words to start and end the sentence
start_word = "I"
end_word = "you"

# Open the file and read its contents
with open(file_name, "r") as file:
    text = file.read()

# Find all sentences that start with the specified word and end with the specified word
sentences = re.findall(f"{start_word}[^.!?]+{end_word}[.!?]", text)

# Print the sentences
for sentence in sentences:
    print(sentence)

