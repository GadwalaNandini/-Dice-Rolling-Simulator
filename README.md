# -Dice-Rolling-Simulator

Time Complexity:
To measure the time complexity, you can analyze the number of operations executed by the program in relation to the input size. This can be done by counting loops, recursion, and any other significant operations.

Space Complexity:
To determine the space complexity, you can examine the amount of memory required by the program as the input size increases. This includes the memory used by variables, data structures, and function calls.

The space complexity is reduced by eliminating any unnecessary variables or data structures. We only use a few variables to store the user's input, the dice roll result, and the choice to roll again.

The program does not involve any data structures that grow with the input size, and the memory usage is limited to a few variables that are reused or overwritten within the loop.

This implementation maintains the functionality of the Dice Rolling Simulator while keeping the space complexity low.

#####  Code Explanation  ######

1. We start by importing the random module, which provides functions for generating random numbers.

2.The main() function serves as the entry point of the program. It contains a while loop that keeps the dice rolling simulator running until the user chooses to quit.

Inside the loop, we use input() to prompt the user to press Enter to roll the dice or 'q' to quit. The user's input is not stored since we are only interested in detecting when they press Enter.

Next, we use random.randint(1, 6) to generate a random number between 1 and 6, representing the roll of a six-sided die. The generated number is stored in the dice_result variable.

We then use print() to display the result of the dice roll to the user, showing the value of dice_result.

Afterward, we use input() again to ask the user if they want to roll the dice again. The user's input is stored in the play_again variable.

If the user enters 'y' (ignoring the case), the loop continues, and the user is prompted to roll the dice again. If the user enters anything other than 'y', the loop is terminated using the break statement.

3.This conditional statement checks if the script is being run directly (not imported as a module) and then calls the main() function to start the dice rolling simulator.


