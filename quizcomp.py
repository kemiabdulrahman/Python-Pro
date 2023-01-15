questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "Rome", "Berlin", "Madrid"], "correct": "Paris"},
    {"question": "What is the largest planet in our solar system?", "choices": ["Earth", "Jupiter", "Mars", "Saturn"], "correct": "Jupiter"},
    {"question": "Who is the author of the Harry Potter series?", "choices": ["J.K. Rowling", "Stephen King", "George R.R. Martin", "Stephenie Meyer"], "correct": "J.K. Rowling"}
]

score = 0

for question in questions:
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i+1}) {choice}")
    user_choice = input("Enter your choice: ")
    if user_choice.lower() == question["correct"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
    print()

print(f"Your final score is: {score}/{len(questions)}")

