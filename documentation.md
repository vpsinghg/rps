**Rock-Paper-Scissors Game**
============================

**Overview**
------------

This is a simple implementation of the classic game of Rock-Paper-Scissors using object-oriented programming principles in Python. The game allows a player to choose between rock, paper, or scissors and then compares the player's choice to the computer's choice to determine the winner. The game also follows SOLID principles for better code design.

**File Structure**
------------------

The game consists of the following files:

*   `game_start.py`: The main file that runs the game.

*   `game.py`: It contains the `Game` class which handles the flow of the game.
    
*   `Strategies/GameStrategy.py`: The file that contains the `GameStrategy` class which defines the Basic Game Strategy class which has  options (rock, paper, and scissors) and their victory graph. This is Abstract Class So it can be used to create different strategies. Like I Created Sheldon Copper Strategy (Sorry BBT Fan).

*   `Strategies/RPSCompareStrategy.py`: The file that contains the `RPSCompareStrategy` class which is the Implementation of GameStrategy Base class and contains options available in particular stretegy and victory graph for different options and finally a compare method which compare the user and computer choice and return result. ***option*** here are rock,paper,scissers.

*   `Strategies/SheldonCopperStrategy.py`: The file that contains the `SheldonCopperStrategy` class which is the Implementation of GameStrategy Base class and contains options available in particular stretegy and victory graph for different options and finally a compare method which compare the user and computer choice and return result. ***option*** here are ***rock, paper, scissers, lizard, spock***.
    
* `input_output.py`: This contains the InputOutput Class which contains the methods get_user_choice and get_computer_choice. Handles the Input Output Logic for Game Class.

*   `logging_config.py`: The file that handles the logging configuration
    
*   `test_game.py`: The file that contains the test functions for testing the `Game` class. It mimics the Strategy and InputOut Classes and test game play method

*  `test_input_output.py`: The file that contains the test functions for testing the `InputOut` class. It mimics the get_user_choice and get_computer_choice methods.
    

**Classes**
-----------

### **InputOutput**

The `InputOutput` class defines the different methods (get_user_choice, get_computer_choice) and their properties.

### **Game**

The `Game` the class handles the flow of the game. 
This recieves the InputOut and GameStrategy class objects which handles the taking inputs from user,computer from the options specifies by the gameStategy 
It has the following methods:


*   `play()`: This method is the entry point of the game. It gets the player's choice, gets the computer's choice, and then checks the result of the game.


### **GameStrategy**
This is Base class for every Game strategy.
It contains 3 abstract methods
* `getOptions` : returns the options available in particular strategy.
* `compare` : compare the given two choices user_choice and computer_choice and return the result.
* `getVictoryGraph` : Returns the victory graph for available game options.

### **RPSCompareStrategy**
This class implements Base `GameStrategy`.
It contains 3 methods
* `getOptions` : returns the options available in RPS strategy which are rock, paper, scissors.
* `compare` : compare the given two choices user_choice and computer_choice and return the result.
* `getVictoryGraph` : Returns the victory graph for available game options. which is
  *  `rock` beats `scissors`
  *  `scissors` beats `paper`
  *  `paper` beats `rock`


### **RPSCompareStrategy (Bonus)**
This class implements Base `GameStrategy`.
It contains 3 methods
* `getOptions` : returns the options available in RPS strategy which are rock, paper, scissors, lizard, spock.
* `compare` : compare the given two choices user_choice and computer_choice and return the result.
* `getVictoryGraph` : Returns the victory graph for available game options. which is
  *  `rock` beats `scissors` and `lizard`.
  *  `scissors` beats `paper` and `lizard`.
  *  `paper` beats `rock` and `spcok`.
  *  `lizard` beats `paper` and `spock`.
  *  `spock` : beats `rock` and `scissors`.





**How to run the game**
-----------------------

To run the game, simply run the `game_start.py` file using a python interpreter


`python game_start.py`

**Logging**
-----------

Logging has been implemented in the game, you can refer to the log file game.log for debugging and tracking the flow of the game.

**Testing**
-----------

Tests have been implemented in the `test_game.py` file, you can run the test by running the following command

`python -m unittest test_game` or `python test_game.py`

**Run Input Out Tests**

`python -m unittest test_input_output` or `python test_input_output.py`


**Conclusion**
--------------

This is a simple implementation of the Rock-Paper-Scissors game that demonstrates the use of object-oriented programming principles in Python. The game can be easily extended to add more options and complexity. The code also follows SOLID principles for better code design.


**Author: Vikram Singh Gurjar (vikramjdh2016@gmail.com)** 
 