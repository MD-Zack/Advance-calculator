Simple Calculator in Python
Welcome to the Simple Calculator project, a command-line based calculator written in Python designed to provide users with an easy-to-use interface for performing basic and essential arithmetic operations. This project serves as an excellent starting point for beginners who want to understand object-oriented programming concepts and error handling in Python while creating a functional and interactive application.

Features and Functionalities
This calculator supports the following operations:

Addition: Adds two numbers and returns the sum.

Subtraction: Calculates the difference between two numbers.

Multiplication: Multiplies two numbers.

Division: Divides one number by another, with built-in handling of division by zero errors to prevent crashes.

Power: Raises a number to the power of another, utilizing Python's math.pow() for accurate calculations.

Square Root: Calculates the square root of two numbers individually using Python's math.sqrt() function.

Clear Screen: Allows users to clear the command line screen for a clean interface (supports Windows with 'cls' command).

The program includes input validation to ensure the user enters valid numeric values, improving user experience and preventing runtime errors. It also provides clear and informative messages to guide the user throughout the operation process.

Design and Implementation
The calculator is implemented using an object-oriented approach with a class named Calc that encapsulates the logic for all operations. This structure promotes code reusability, clarity, and scalability. Each arithmetic operation is represented as a method within the class, making it easy to maintain and extend.

The user interface runs in a continuous loop, displaying a menu of options and prompting the user for input until the user decides to exit. The design includes error handling for invalid input types and division by zero to make the program robust.

Potential Improvements and Extensions
While this simple calculator covers basic arithmetic, it lays the foundation for future enhancements such as:

Adding support for more complex mathematical functions (e.g., logarithms, trigonometric functions).

Implementing a graphical user interface (GUI) to enhance user interaction.

Supporting multi-step calculations without restarting the program.

Including unit tests to ensure reliability and correctness.

Enhancing cross-platform compatibility for clear screen commands.

Usage
To run this calculator, simply execute the Python script in your terminal or command prompt. Follow the on-screen instructions to select your desired operation and input the numbers. The program will display the result immediately and return to the menu for further calculations until you choose to exit.

Conclusion
This project is an excellent exercise for beginners to practice Python programming concepts such as classes, methods, exception handling, and user input management. It also demonstrates how to create a user-friendly command-line interface application. Feel free to explore, modify, and expand upon this calculator to fit your learning goals or project needs.

