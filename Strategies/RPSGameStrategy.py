from Strategies.GameStrategy import GameStrategy
import logging

class RPSCompareStrategy(GameStrategy):
    """Comparison strategy for Rock-Paper-Scissors game"""

    def __init__(self):
        self.options = ['rock','paper','scissors']
        self.victoryGraph = {
            'rock' : ['scissors'],
            'paper' : ['rock'],
            'scissors' : ['paper'],
        }
        logging.info('Initializing Strategy for Rock-Paper-Scissors game')
    
    def getOptions(self):
        return self.options
    
    def getVictoryGraph(self):
        return self.victoryGraph

    def compare(self, user_choice, computer_choice):
        if user_choice not in self.options:
            raise ValueError("Invalid choice. Please select from: rock, paper, scissors.")
        if computer_choice not in self.options:
            raise ValueError("Invalid choice. Please select from: rock, paper, scissors.")
        if user_choice == computer_choice:
            return "Tie"
        elif computer_choice in self.victoryGraph[user_choice]:
            return "You win!"
        else:
            return "You lose!"