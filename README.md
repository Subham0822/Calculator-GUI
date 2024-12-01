# GUI Calculator in Python

A simple and visually appealing calculator application built using **Tkinter** in Python. This project demonstrates the use of Tkinter for GUI-based applications and basic arithmetic operations.

## Features
- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division.
- **Clear Input**: Erase the current input with a single button.
- **Error Handling**: Displays "Error" for invalid expressions.
- **Interactive Buttons**: Numeric and operation buttons are color-coded for usability.
- **Responsive UI**: Adjusted for seamless user interaction.

## Color Scheme
- **Background**: Dark gray-blue (`#2D2D2D`).
- **Button Colors**:
  - **Digits (`0-9`)**: Green (`#4CAF50`) background with Royal Blue (`#4169E1`) text.
  - **Operators (`+`, `-`, `*`, `/`)**: Blue (`#2196F3`) background with Royal Blue (`#4169E1`) text.
  - **Clear (`CE`)**: Red (`#F44336`) background with Royal Blue (`#4169E1`) text.
  - **Equal (`=`)**: Orange (`#FF9800`) background with Royal Blue (`#4169E1`) text.
- **Input Field**: Light gray (`#E0E0E0`) background with black text.

## Screenshot
[Click Here](screenshot.png)

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/calculator-tkinter.git

2. Navigate to the project directory:
   ```bash
   cd calculator-tkinter

3. Run the Python script:
   ```bash
   python calculator.py

## Usage
- Run the script to open the calculator.
- Use the numeric and operator buttons to create expressions.
- Press the "=" button to calculate the result.
- Use "CE" to clear the input field.

## Project Structure
  ```bash
  calculator-tkinter/
│
├── calculator.py      # Main Python script
├── screenshot.png     # Sample screenshot
├── LICENSE
├── README.md          # Project documentation
└── .gitignore         # Git ignore file (if any sensitive files)
```
## How It Works
- The calculator uses the eval() function to evaluate arithmetic expressions entered through the GUI.
- Tkinter handles the creation and placement of buttons and the input field.

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue for improvements.

## License

This project is licensed under the [MIT License](LICENSE).
