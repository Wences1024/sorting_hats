# Sorting Hat Simulation

This project implements a simple simulation of the Sorting Hat from the Harry Potter series. The program assigns a random Hogwarts house to the user each time they press the `space` key. The simulation continues until the user presses the `esc` key to exit.

## Features
- Assigns a random Hogwarts house: `Hufflepuff`, `Gryffindor`, `Ravenclaw`, or `Slytherin`.
- Interactive functionality using the keyboard:
  - Press `space` to get assigned a house.
  - Press `esc` to exit the program.

## Prerequisites
Ensure you have the following Python library installed:
- `keyboard` (for detecting key presses)

To install it, use the following command:
```bash
pip install keyboard
```

## How to Run
1. Save the code in a file named, for example, `sorting_hat.py`.
2. Run the script using Python:
   ```bash
   python sorting_hat.py
   ```
3. Follow the on-screen instructions:
   - Press `space` to get a house assignment.
   - Press `esc` to exit the program.

## Code Overview
The script contains the following components:

### `Sorting` Class
- **Attributes:**
  - `houses`: A list of Hogwarts houses.
- **Methods:**
  - `House_Selection()`: Randomly selects and returns a house from the `houses` list.

### Main Functionality
- Creates an instance of the `Sorting` class.
- Continuously listens for key presses:
  - Assigns a house when `space` is pressed.
  - Exits when `esc` is pressed.

## Example Output
```
La casa que el sombrero me asigno fue: Gryffindor
La casa que el sombrero me asigno fue: Slytherin
```

## Notes
- The program uses a `time.sleep(1)` delay to prevent multiple house assignments when holding the `space` key.
- Ensure you have the necessary permissions to detect key presses on your system.

## License
This project is open-source.
