from game import Game 
from Strategies.RPSGameStrategy import RPSCompareStrategy
from Strategies.SheldonCopperStrategy import SheldonCopperStrategy
from input_output import InputOutput
from logging_config import setup_logging

if __name__ == "__main__":
    setup_logging()
    # strategy1 = RPSCompareStrategy()
    # strategy2 = SheldonCopperStrategy()
    # game = Game(compare_strategy =strategy)

    # default Game
    game = Game() 
    result = game.play()
