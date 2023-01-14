import random
quiz = {
    "What is the capital of France?": "Paris",
    "What is the currency of Japan?": "Yen",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the smallest planet in our solar system?": "Mercury"
}

random_quiz = [question for question in quiz]
random.shuffle(random_quiz)
score = 0

for question in random_quiz:
    answer = input(question + " ")
    if answer.lower() == quiz[question].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", quiz[question])

print("Your final score is", score, "out of", len(quiz))

