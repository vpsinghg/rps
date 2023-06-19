from typing import List
import logging

class InputOutput:
    """Handles input/output for the game.
    """
    def __init__(self):
        logging.info('Initializing InputOut Service for Rock-Paper-Scissors game')
        pass


    def get_user_choice(self, choices:List) -> str:
        """Get user's choice.
        """
        n = len(choices)
        joinedChoices = ", ".join(choices[0:n-1]) + " or " + choices[n-1]
        inputMessage =f"Enter one option from {joinedChoices}: "
        user_choice = input(inputMessage)
        return user_choice

    def get_computer_choice(self,choices:List) -> str:
        """Get computer's choice.
        """
        import random
        computer_choice = random.choice(choices)
        return computer_choice

    def display_result(self, result: str) -> None:
        """Display the result of the game.
        """
        print("Result: ", result)