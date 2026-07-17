# -------------------------------
#        QUIZ APPLICATION
# -------------------------------

# List of quiz questions
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which language is primarily used for Data Science?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "3. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "5. What is the output of 5 + 3 * 2?",
        "options": ["A. 16", "B. 11", "C. 13", "D. 10"],
        "answer": "B"
    }
]

score = 0

print("=" * 50)
print("         WELCOME TO THE QUIZ")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello, {name}! Let's begin the quiz.\n")

# Quiz loop
for q in questions:

    print(q["question"])

    for option in q["options"]:
        print(option)

    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C, or D.")

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}.\n")

# Result
print("=" * 50)
print("              QUIZ RESULT")
print("=" * 50)

print("Name :", name)
print("Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    grade = "A"
    message = "Excellent!"
elif percentage >= 60:
    grade = "B"
    message = "Good Job!"
elif percentage >= 40:
    grade = "C"
    message = "Keep Practicing!"
else:
    grade = "F"
    message = "Better Luck Next Time!"

print("Grade:", grade)
print(message)

print("=" * 50)
print("Thank you for playing!")