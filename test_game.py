import unittest
from game import Game

class TestGame(unittest.TestCase):
    def test_play(self):
        # Create a mock RPSCompareStrategy object
        class MockRPSCompareStrategy:
            def getOptions(self):
                return ["rock", "paper", "scissors"]
            def compare(self, choice1, choice2):
                return "tie"
        
        # Create a mock InputOutput object
        class MockInputOutput:
            def get_user_choice(self, options):
                return "rock"
            def get_computer_choice(self, options):
                return "rock"
        
        game = Game(compare_strategy=MockRPSCompareStrategy(), input_output=MockInputOutput())
        self.assertEqual(game.play(), "tie")
        
    def test_play_win(self):
        # Create a mock RPSCompareStrategy object
        class MockRPSCompareStrategy:
            def getOptions(self):
                return ["rock", "paper", "scissors"]
            def compare(self, choice1, choice2):
                if choice1 == "rock" and choice2 == "scissors":
                    return "win"
                return "lose"
        
        # Create a mock InputOutput object
        class MockInputOutput:
            def get_user_choice(self, options):
                return "rock"
            def get_computer_choice(self, options):
                return "scissors"
        
        game = Game(compare_strategy=MockRPSCompareStrategy(), input_output=MockInputOutput())
        print("Game Play Function Testing Started")
        self.assertEqual(game.play(), "win")
        print("Game Play Function Tested.")


        
    def test_play_lose(self):
        # Create a mock RPSCompareStrategy object
        class MockRPSCompareStrategy:
            def getOptions(self):
                return ["rock", "paper", "scissors"]
            def compare(self, choice1, choice2):
                if choice1 == "rock" and choice2 == "scissors":
                    return "win"
                return "lose"
        
        # Create a mock InputOutput object
        class MockInputOutput:
            def get_user_choice(self, options):
                return "scissors"
            def get_computer_choice(self, options):
                return "rock"
        
        game = Game(compare_strategy=MockRPSCompareStrategy(), input_output=MockInputOutput())
        self.assertEqual(game.play(), "lose")

if __name__ == '__main__':
    unittest.main()
