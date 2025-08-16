import requests  # For making HTTP requests to fetch questions
import html      # To decode HTML entities in question/answer text
import random    # For shuffling answer options

# Function to fetch questions from Open Trivia DB API
def fetch_questions(amount=15, qtype="multiple"):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,  # Number of questions to fetch
        "type": qtype      # Type of question: "multiple" means multiple-choice
    }

    response = requests.get(url, params=params)  # Send request to API
    data = response.json()  # Parse JSON response

    # Check if API returned success
    if data.get("response_code") != 0:
        print("⚠️ Error fetching questions from the API.")
        return []  # Return empty list if API fails

    questions = []
    for item in data["results"]:
        # Decode HTML entities in questions and answers
        question = html.unescape(item["question"])
        correct_answer = html.unescape(item["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in item["incorrect_answers"]]

        # Combine correct and incorrect answers and shuffle them
        options = incorrect_answers + [correct_answer]
        random.shuffle(options)

        # Append formatted question data to the list
        questions.append({
            "question": question,
            "options": options,
            "correct_answer": correct_answer
        })
    return questions  # Return list of formatted questions

# Main game function
def kbc_game():
    total_questions = 15  # Total number of questions in the game
    questions = fetch_questions(total_questions)  # Get questions from API

    # Exit if no questions were returned
    if not questions:
        print("❌ No questions available. Try again later.")
        return

    # Prize money for each question level
    prize_money_list = [
        1000, 2000, 3000, 5000, 10000,
        20000, 40000, 80000, 160000, 320000,
        640000, 1250000, 2500000, 5000000, 10000000
    ]

    total_won = 0  # Track the total amount won by the player
    lifeline_50_50_used = False  # Track whether 50-50 lifeline is used
    lifeline_skip_used = False   # Track whether skip lifeline is used

    # Game introduction
    print("\n🎮 Welcome to KBC 🎮\n")
    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1} for ₹{prize_money_list[i]}:")
        print(q["question"])  # Display the question

        # Ask user if they want to use a lifeline
        lifeline_choice = input("Use a lifeline? (type 'lifeline 1', 'lifeline 2', or 'none'): ").strip().lower()

        options_to_show = q["options"].copy()  # Copy all answer options

        # Handle 50-50 lifeline
        if lifeline_choice == "lifeline 1":
            if lifeline_50_50_used:
                print("❌ 50-50 lifeline already used.")
            else:
                lifeline_50_50_used = True
                # Keep correct answer, randomly select one wrong answer
                options_to_show = [q["correct_answer"]]
                wrongs = [opt for opt in q["options"] if opt != q["correct_answer"]]
                options_to_show += random.sample(wrongs, 1)  # Add one random incorrect option
                random.shuffle(options_to_show)  # Shuffle for fairness
                print("🧪 50-50 Lifeline activated!")

        # Handle skip lifeline
        elif lifeline_choice == "lifeline 2":
            if lifeline_skip_used:
                print("❌ Skip lifeline already used.")
            else:
                lifeline_skip_used = True
                print("⏭️ You skipped this question. No prize for this one.")
                continue  # Skip to the next question without earning prize

        # Display answer options as A, B, C, D
        for idx, option in enumerate(options_to_show):
            print(f"  {chr(65 + idx)}. {option}")

        # Get user's answer
        user_input = input("Your answer (A/B/C/D): ").strip().upper()

        # Validate user input and map it to an answer
        if user_input in "ABCD" and (ord(user_input) - 65) < len(options_to_show):
            selected_option = options_to_show[ord(user_input) - 65]
        else:
            print("❌ Invalid input. Game over.")
            break  # End game if input is invalid

        # Check if selected answer is correct
        if selected_option == q["correct_answer"]:
            total_won += prize_money_list[i]  # Add prize to total
            print(f"✅ Correct! You've won ₹{prize_money_list[i]}")
        else:
            print(f"❌ Wrong answer. The correct answer was: {q['correct_answer']}")
            break  # End game on wrong answer

    # Final result after game ends
    print(f"\n🏆 Game Over! Total amount won: ₹{total_won}")
    print("🙏 Thank you for playing KBC!")

# Run the game
kbc_game()