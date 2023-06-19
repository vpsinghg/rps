import unittest
from unittest.mock import patch
from input_output import InputOutput

class TestInputOutput(unittest.TestCase):
    def setUp(self):
        self.input_output = InputOutput()
        self.choices = ['rock', 'paper', 'scissor']

    @patch('builtins.input', return_value='rock')
    def test_get_user_choice(self, input_mock):
        print("InputOutput Class Method get_user_choice Testing Started")
        result = self.input_output.get_user_choice(self.choices)
        self.assertEqual(result, 'rock')
        print("InputOutput Class Method get_user_choice Tested")

    def test_get_computer_choice(self):
        print("InputOutput Class Method get_computer_choice Testing Started")
        result = self.input_output.get_computer_choice(self.choices)
        self.assertIn(result, self.choices)
        print("InputOutput Class Method get_computer_choice Tested")

if __name__ == '__main__':
    unittest.main()