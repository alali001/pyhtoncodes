import random

def quiz():
    # List of countries and their capitals
    quiz_questions = {
        "Saudi Arabia": "Riyadh",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Portugal": "Lisbon",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Qatar": "Doha",
        "Pakistan": "Islamabad",
        "Greece": "Athens"
    }

    print("="*50)
    print("🌍 Welcome to the Countries & Capitals Quiz! 🌍\n")
    print("Type your answer and press Enter. You can type 'skip' to skip a question.\n")

    score = 0
    total_questions = len(quiz_questions)

    # Shuffle questions
    questions = list(quiz_questions.items())
    random.shuffle(questions)

    for i, (country, capital) in enumerate(questions, start=1):
        user_answer = input(f"{i}. What is the capital of {country}? ").strip().lower()

        if user_answer == "skip":
            print(f"Skipped! The correct answer was: {capital}\n")
            continue

        if user_answer == capital.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {capital}\n")

    percentage = (score / total_questions) * 100

    print("="*50)
    print(f"🎯 Quiz Completed! You scored {score} out of {total_questions}.")
    print(f"Your percentage: {percentage:.1f}%")

    if percentage == 100:
        print("🏆 Excellent! You got all correct!")
    elif percentage >= 70:
        print("👏 Great job!")
    elif percentage >= 50:
        print("👍 Not bad, keep practicing!")
    else:
        print("📚 Better luck next time!")

if __name__ == "__main__":
    quiz()