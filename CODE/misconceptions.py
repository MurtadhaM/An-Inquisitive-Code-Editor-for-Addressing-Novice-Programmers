"""
A collection of functions that demonstrate common misconceptions about Python.
"""
from  logging import getLogger
logger = getLogger(__name__)

class Misconception:
    """A class that demonstrates common misconceptions about Python."""
    def __init__(self):
        pass
    
    
    def i_will_exit(self):
        """This function demonstrates the use of the break statement."""
        print("I_will_exit() called")
        # This while loop will continue to execute until the user enters 'exit'
        while True:
            user_input = input("Enter 'exit' to end the loop: ")
            # If the user enters 'exit', we will break out of the loop
            if user_input == 'exit':
                break
            # We will log the user's input to the terminal
            logger.info(user_input)
            
    # is_equal() is used to compare two values to see if they are equal.
    def is_equal(self):
        """This function compares two values to see if they are equal."""
        # This function continually asks for user input until they enter "exit"
        # Keep looping until we break out
        while True:
            # Ask the user for input
            user_input = input("Enter 'exit' to end the loop: ")
            # If the user entered "exit", then break out of the loop
            if user_input == 'exit':
                break

    def double_negative(self):
        """This function demonstrates the use of double negatives."""
        print("double_negative() called")
        # This while loop runs until the user enters 'exit'.
        while True:
            # This line asks the user for input.
            user_input = input("Enter 'exit' to end the loop: ")
            # This if statement checks if the user has entered 'exit'.
            if user_input == 'exit':
                # If the user has entered 'exit', this break statement ends the loop.
                break

    # recursive() is used to call itself.
    def recursive(self):
        """This function recursively calls itself until the user enters 'exit'."""
        user_input = input("Enter 'exit' to end the loop: ")
        if user_input == 'exit':
            return None
        self.recursive()
        return None

    def exception_handling(self):
        """This function handles exceptions."""
        while True:
            try:
                user_input = input()
            except ValueError as ve:
                logger.error(ve)
            except FileNotFoundError as fnf:
                logger.error(fnf)
            except KeyboardInterrupt:
                logger.error("Keyboard interrupt occurred")
            if user_input == 'exit':
                break
        return None
    def __str__(self):
        return "Misconception()"
