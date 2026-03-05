from logic_utils import *
# --- check_guess ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_invalid_input():
    # Non-integer guess should return "Invalid Input"
    outcome, _ = check_guess("fifty", 50)
    assert outcome == "Invalid Input"


# --- parse_guess ---

def test_parse_guess_valid():
    ok, value, _ = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42

def test_parse_guess_empty():
    ok, _, err = parse_guess("", 1, 100)
    assert ok is False
    assert err == "Enter a guess."

def test_parse_guess_not_a_number():
    ok, _, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert err == "That is not a number."

def test_parse_guess_out_of_range_high():
    ok, _, err = parse_guess("101", 1, 100)
    assert ok is False
    assert err == "Guess must be between 1 and 100."

def test_parse_guess_out_of_range_low():
    ok, _, err = parse_guess("0", 1, 100)
    assert ok is False
    assert err == "Guess must be between 1 and 100."

def test_parse_guess_boundary_low():
    ok, value, _ = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1

def test_parse_guess_boundary_high():
    ok, value, _ = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100


# --- update_score ---

def test_update_score_win_normal():
    # Score should be unchanged on a win above minimum
    assert update_score(80, "Win", 3) == 80

def test_update_score_win_below_minimum():
    # Score below 10 should be bumped to 10 on a win
    assert update_score(5, "Win", 10) == 10

def test_update_score_too_high():
    assert update_score(80, "Too High", 1) == 70

def test_update_score_too_low():
    assert update_score(80, "Too Low", 1) == 70

def test_update_score_unknown_outcome():
    # Unknown outcome should leave score unchanged
    assert update_score(80, "Invalid Input", 1) == 80


# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_range_unknown_defaults_to_normal():
    assert get_range_for_difficulty("Unknown") == (1, 100)
