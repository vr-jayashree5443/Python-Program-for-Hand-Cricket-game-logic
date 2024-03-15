# Python-Program-for-Hand-Cricket-game-logic

### 1. `score` Function:
#### Purpose:
- Calculates the score for each player (user and computer) during a cricket game.
- Handles the logic of user and computer input during each ball of an inning.

#### Parameters:
- `bat`: An integer (0 or 1) representing who is batting (0 for user, 1 for computer).
- `bowl`: An integer (0 or 1) representing who is bowling (0 for user, 1 for computer).
- `innings`: An integer representing the current inning (1 for first inning, 2 for second inning).
- `user_score`: The current score of the user.
- `computer_score`: The current score of the computer.

#### Logic:
- A loop runs until the user and computer choose the same number during a ball.
- During each iteration of the loop:
  - Prints the ball number.
  - Gets the user's input (number of runs) and adds it to the user's score.
  - Generates a random number (computer's runs) and adds it to the computer's score.
  - Checks if the user and computer chose the same number. If so, the loop breaks.
- If it's the second inning, it checks if the target score is achieved, and breaks the loop accordingly.
- Finally, it prints the user's or computer's score based on the batting side.
- Returns the updated `user_score` and `computer_score`.

### 2. `Hand_Cricket` Function:
#### Purpose:
- Simulates a hand cricket game between the user and the computer.

#### Logic:
- Asks the user to choose "Odd" or "Even" for the toss.
- Calculates the total toss value.
- Based on the toss result, determines who won the toss and who chose "bat" or "bowl".
- Simulates the first inning using the `score` function with `innings` set to 1.
- Swaps batting and bowling sides for the second inning.
- Simulates the second inning using the `score` function with `innings` set to 2.
- Determines the winner based on the scores.
- Returns the winner (0 for draw, 1 for user, 2 for computer).

### 3. Main Execution:
- Calls `Hand_Cricket` to play the first game.
- Asks the user for the number of matches (`n`) they want to play.
- Runs a loop for `n` matches:
  - Asks if the user wants to continue to the next match.
  - Plays the next match using `Hand_Cricket`.
  - Updates the `win_matches` dictionary based on the match result.
  - Calculates the points for each player based on the match result.
- Prints the final points table (`points_table`) showing the number of wins and points for each player.
- Outputs the total number of matches won by the computer (`win_matches['computer']`).

### Explanation:
This Python script simulates a hand cricket game where the user plays against the computer. It includes two main functions:
- `score`: Calculates the score for each player during a cricket inning.
- `Hand_Cricket`: Manages the game flow, including toss, innings, score calculation, and determining the winner.

The script allows the user to play multiple matches against the computer, keeps track of the wins, and displays a final points table at the end.

### Example Output:
![image](https://github.com/vr-jayashree5443/Python-Program-for-Hand-Cricket-game-logic/assets/128161257/190529ce-2a0f-4db5-862a-163702de388e)
