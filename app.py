import random
import streamlit as st
from logic_utils import *

#function that initializes the game state
def initialize_game_state(low, high, difficulty="Normal"):
    st.session_state.secret = random.randint(low, high)
    st.session_state.difficulty = difficulty
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.message = None


def show_debug_info(difficulty):
    with st.expander("Developer Debug Info"):
        st.write("Secret:", st.session_state.secret)
        st.write("Attempts:", st.session_state.attempts)
        st.write("Score:", st.session_state.score)
        st.write("Difficulty:", difficulty)
        st.write("History:", st.session_state.history)




#main app code

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")


#refactored
if not st.session_state:
    initialize_game_state(low, high)
elif st.session_state.get("difficulty") != difficulty:
    initialize_game_state(low, high, difficulty)



st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

#refactored
show_debug_info(difficulty)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.is_new_game = True
    initialize_game_state(low, high, difficulty)
    st.rerun()

#show new game banner if new game was just started
if st.session_state.get("is_new_game"):
    st.success("🎮 New Game Started! 🎮")
    st.session_state.is_new_game = False

if st.session_state.status != "playing":
    if st.session_state.status == "won":
            st.balloons()
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
    elif st.session_state.attempts >= attempt_limit:
            st.error(
                f"Out of attempts! "
                f"The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )
    pass
    # if st.session_state.status == "won":
    #     st.success("You already won. Start a new game to play again.")
    # else:
    #     st.error("Game over. Start a new game to try again.")
    # st.stop()  
elif st.session_state.get("message") and show_hint:
    st.warning(st.session_state.message) 

if submit:
    #check if game is already over
    if st.session_state.status != "playing":
        if st.session_state.status == "won":
            st.success("You already won. Start a new game to play again.")
        else:
            st.error("Game over. Start a new game to try again.")
        st.stop()  

    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess, low, high)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # if st.session_state.attempts % 2 == 0:
        #     secret = int(st.session_state.secret)
        # else:
        #      secret = st.session_state.secret
        secret = st.session_state.secret

        outcome, st.session_state.message = check_guess(guess_int, secret)

        # if show_hint:
        #     st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.status = "won"
            st.rerun()
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.rerun()

        # if outcome == "Win":
        #     st.balloons()
        #     st.session_state.status = "won"
        #     st.success(
        #         f"You won! The secret was {st.session_state.secret}. "
        #         f"Final score: {st.session_state.score}"
        #     )
        # else:
        #     if st.session_state.attempts >= attempt_limit:
        #         st.session_state.status = "lost"
        #         st.error(
        #             f"Out of attempts! "
        #             f"The secret was {st.session_state.secret}. "
        #             f"Score: {st.session_state.score}"
        #         )

    if st.session_state.status == "playing":
        st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
