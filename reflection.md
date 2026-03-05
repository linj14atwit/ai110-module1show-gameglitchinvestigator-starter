# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

time spent: 3h 30m
## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. The feedback telling go high or low is giving misinformation
2. low high message is not reflected when difficulty change
3. secret is not updated on difficulty change resulted in secret out of low high range
4. entering numbers out of range still consumed attempts
5. attempts not working properly
6. banners, developer info not updating in time  
7. score and attempts not reseting on new game
8. new game not working after game won
9. (found late) scoring system is weird


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used mainly claude and copilot for this project. 
- There was a part where I wanted to refactor code and have game state resetted on difficulty change. I created initialize_game_state function with the help of copilot code completing, it however had issues where some variables might not have been defined during the call. Claude helped me identified the dependency issues and suggested a fix by passing the varible through as parameters. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I firstly rely on my own judgement, if the program was doing something unintended and now it is not, I would declare it as fixed. I then would use AI generated test cases which is more exhaustive to help me confirm my judgement.
- I mainly used AI generated test cases for logical functions and manually play tested other fixes such as display.
- AI helped me generated my test cases, I prompted it to structure and format the tests in a way that is easy for me to read and understand so I can quickly skim through it to get a good grasp of it.
I could also ask other AI models to further confirm the tests.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?


- What change did you make that finally gave the game a stable secret number?

- The secret number wasn't changing on the version I recieved, or maybe I didn't notice it and it was fixed along side other bugs.
- Everytime rerun is called, the page is refreshed and the whole application code is executed again. Top to bottom. Thus rerun.
- I refactored the initialization process into a function, removed all instances of secret number being updated and have a new secret number generated only on the initialization function.
The function is called when the app is first launched, on new game, and difficulty changes.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- It would be using test cases to help verify the code is working as intended even after changes such as refactoring.
- If possible, I want to try and utilize AI tools more, I mainly use AI not as generative tool but rather an inspection tool to help me understand the code and find parts where I need to change. I also use the generated code to give me an idea of how to fix it, sometimes the suggestion is applied sometimes not.
I probably would have done so if the code is more complicated or if the language/library is something I am not familiar with.