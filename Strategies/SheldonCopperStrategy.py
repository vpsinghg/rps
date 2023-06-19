from Strategies.GameStrategy import GameStrategy
import logging

class SheldonCopperStrategy(GameStrategy):
    """Comparison strategy for Rock-Paper-Scissors-Lizard-Spock game"""

    def __init__(self):
        self.options = ['rock','paper','scissors','lizard','spock']
        self.victoryGraph = {
            'rock' : ['scissors' ,'lizard'],
            'paper' : ['rock','spock'],
            'scissors' : ['paper','lizard'],
            'lizard' : ['paper','spock'],
            'spock' : ['rock','scissors']
        }
        logging.info('Initializing Strategy for Rock-Paper-Scissors-Lizard-Spock game')
    
    def getOptions(self):
        return self.options
    
    def getVictoryGraph(self):
        return self.victoryGraph

    def compare(self, user_choice, computer_choice):
        if user_choice not in self.options:
            raise ValueError("Invalid choice. Please select from: rock, paper, scissors, lizard, spock.")
        if computer_choice not in self.options:
            raise ValueError("Invalid choice. Please select from: rock, paper, scissors, lizard, spock.")
        if user_choice == computer_choice:
            return "Tie"
        elif computer_choice in self.victoryGraph[user_choice]:
            return "You win!"
        else:
            return "You lose!"