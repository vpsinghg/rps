import abc
from typing import List
import logging
from Strategies.RPSGameStrategy import RPSCompareStrategy
from input_output import InputOutput

class Game:
    """Main game class for Rock-Paper-Scissors"""
    def __init__(self, compare_strategy=None,input_output = None,):
        self.compare_strategy = compare_strategy or RPSCompareStrategy()
        self.input_output = input_output or InputOutput()
        logging.info("Initializing Game With {options}".format(options=self.compare_strategy.getOptions()))
        
    def play(self):
        """ Take User Input Using InputOutput Service """
        availableOptions = self.compare_strategy.getOptions()
        user_choice = self.input_output.get_user_choice(availableOptions)
        computer_choice = self.input_output.get_computer_choice(availableOptions)

        """play game with user choice"""
        result = self.compare_strategy.compare(user_choice, computer_choice)
        logging.info(f'user_choice: {user_choice}, computer_choice: {computer_choice}, result: {result}')
        return result
