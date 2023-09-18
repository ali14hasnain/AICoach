# app.py

from ai_coach import AICoach

def main():
    # Initialize the AICoach
    ai_coach = AICoach()

    # Get user input or text to analyze
    user_input = input("Enter the text you want to improve: ")

    # Analyze the text and provide feedback
    coaching_result = ai_coach.get_coaching_result(user_input)

    # Display the coaching result to the user
    print(coaching_result)

if __name__ == "__main__":
    main()
