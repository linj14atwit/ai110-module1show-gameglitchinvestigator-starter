def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    #edited
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    #check if it is a number
    try:
        float(raw)
    except ValueError:
        return False, None, "That is not a number."

    value = int(raw)

    #check if it is in range
    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    #fixed logic
    if not isinstance(guess, int):
        return "Invalid Input", "❌ Please enter a valid integer."

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    else:
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # points = 10 * (attempt_number + 1)
        if current_score < 10:
            #minimun point of 10 for winning
            current_score = 10
        return current_score

    if outcome == "Too High":
        #remove weird logic code
        # if attempt_number % 2 == 0:
        #     return current_score + 5
        return current_score - 10

    if outcome == "Too Low":
        return current_score - 10

    return current_score
