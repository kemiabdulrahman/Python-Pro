import random

# Dictionary containing the questions and answers
quiz = {
    ("Math", "What is the value of pi?"): "3.14",
    ("Math", "What is the square root of 9?"): "3",
    ("Math", "What is the formula for the area of a circle?"): "pi * r^2",
    ("Science", "What is the symbol for gold on the periodic table?"): "Au",
    ("Science", "What is the smallest planet in our solar system?"): "Mercury",
    ("Science", "What is the study of fossils called?"): "Paleontology"
}

# Group questions by subject
questions_by_subject = {}
for question, answer in quiz.items():
    subject = question[0]
    if subject not in questions_by_subject:
        questions_by_subject[subject] = []
    questions_by_subject[subject].append((question[1],answer))

# Shuffle the questions within each subject
for subject in questions_by_subject:
    random.shuffle(questions_by_subject[subject])
    
# Take the quiz
score = 0
for subject in questions_by_subject:
    print(f"Subject: {subject}")
    for question,answer in questions_by_subject[subject]:
        response = input(question + " ")
        if response.lower() == answer.lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect. The correct answer is", answer)
    print()

print("Your final score is", score, "out of", len(quiz))

