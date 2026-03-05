#refactored logic functions with Claude AI

def get_range_for_difficulty(difficulty: str):
    """
    Return the (low, high) number range for a given difficulty.

    Args:
        difficulty: "Easy", "Normal", or "Hard"

    Returns:
        Tuple[int, int]: (low, high) inclusive bounds.
        Defaults to (1, 100) for unknown difficulties.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    """
    Parse and validate raw user input as an integer guess within range.

    Args:
        raw: Raw string input from the user.
        low: Minimum allowed value (inclusive).
        high: Maximum allowed value (inclusive).

    Returns:
        Tuple of (ok, guess_int, error_message):
            ok (bool): True if input is valid.
            guess_int (int | None): Parsed integer, or None if invalid.
            error_message (str | None): Error string, or None if valid.
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
    Compare a guess against the secret number.

    Args:
        guess: The player's guess. Must be an int to be valid.
        secret (int): The secret number to guess.

    Returns:
        Tuple[str, str]: (outcome, message)
            outcome: One of "Win", "Too High", "Too Low", or "Invalid Input".
            message: A user-facing hint string.
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
    """
    Calculate the new score based on the outcome of a guess.

    Args:
        current_score: The player's current score.
        outcome: Result from check_guess — "Win", "Too High", or "Too Low".
        attempt_number: The current attempt count (1-indexed).

    Returns:
        int: Updated score. Deducts 10 for wrong guesses.
             On a win, ensures score is at least 10.
    """
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
