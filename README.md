# Indian States and UTs Game

This Python program is an educational game where players guess the names of Indian States and Union Territories (UTs). Each correct guess places the name of the state/UT on its geographical location on an interactive map of India.

## Game Features

- **Interactive Learning**: Players can learn the locations of Indian States and UTs through repeated guesses.
- **Map Display**: The game shows an image of India with correct guesses displayed at the state's/UT's location.
- **Progress Tracking**: Displays the number of correct answers out of 37 total states/UTs.
- **Learning Aid**: If the player exits the game early, a file `areas_to_learn.csv` is created with the names of states/UTs not yet guessed, helping players focus on areas they missed.

## How to Play

1. **Start the Game**: Run the program, which opens a map of India.
2. **Input Guesses**: Type the name of an Indian State or UT in the prompt that appears.
3. **Check Your Progress**: The title displays the count of correct guesses out of 37.
4. **Exit and Review**: Type "Exit" to end the game early, and an `areas_to_learn.csv` file will be saved with the names of any states/UTs you missed.

## Code Explanation

The program uses the `turtle` and `pandas` libraries to handle graphics and data:

1. **Setup**:
   - Displays an image of India on a Turtle screen.
   - Reads `India States-UTs.csv` to get state/UT names along with latitude and longitude coordinates.

2. **Coordinate Transformation**:
   - Converts latitude/longitude coordinates to x/y positions on the image based on predefined scales.

3. **Game Loop**:
   - Continuously prompts the user for a state/UT name.
   - If the name matches a state/UT, it is displayed at the correct location on the map.
   - If "Exit" is entered, the program saves a list of missing states/UTs to a CSV file.

## File Structure

- `main.py`: The main script to run the game.
- `Indian States and UTs GIF.gif`: The background map image.
- `India States-UTs.csv`: A data file containing state/UT names and their latitude/longitude coordinates.
- `areas_to_learn.csv`: A file generated upon exiting early, listing unguessed states/UTs.
