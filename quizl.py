questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "Rome", "Berlin", "Madrid"],
        "correct": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Earth", "Jupiter", "Mars", "Saturn"],
        "correct": 1
    },
    {
        "question": "Who is the author of the Harry Potter series?",
        "choices": ["J.K. Rowling", "Stephen King", "George R.R. Martin", "Stephenie Meyer"],
        "correct": 0
    }
]

score = 0

for question in questions:
    print(question["question"])
    for i in range(len(question["choices"])):
        print(str(i) + ") " + question["choices"][i])
    user_choice = int(input("Enter your choice: "))
    if user_choice == question["correct"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
    print()

print("Your final score is: " + str(score) + "/" + str(len(questions)))

