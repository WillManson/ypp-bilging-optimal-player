# ypp-bilging-optimal-player
A project to find optimal sequences of moves for the bilging puzzle in the game Yohoho! Puzzle Pirates by Three Rings Design.

Word of caution: using this script got me banned from the game. Use at your own risk.

The script can read the pieces from the board and find the optimal sequence of moves of length less than or equal to some given number n (which is passed to the getOptimalSequenceOfMoves method). I have found that the script works pretty well with n = 2. Setting n = 3 gives a massive boost in score, but can take a while to compute (which can negate the increase in score benefit for sufficiently slow machines, due to the nature of in-game scoring). The script can also automatically enter the moves into the game.

The script requires that you have installed:
* [PIL](http://www.pythonware.com/products/pil/) or [Pillow](https://pillow.readthedocs.org/) (the latter is slightly easier to install)
* [pyscreenshot](https://github.com/ponty/pyscreenshot)
* [PyUserInput](https://github.com/SavinaRoja/PyUserInput)

To use my program, do the following:
* Install the above modules
* Make a local of my scripts
* Open Puzzle Pirates and start the bilging puzzle
* Open a terminal window and make sure that it is not blocking your view of the 6-by-12 grid of bilging puzzle pieces
* In the terminal window, browse to my scripts
* Type `python board.py`, but do not hit enter
* Hover your mouse over the top-left piece of the bilging puzzle
* With the terminal still in focus, hit enter
* Follow the prompts shown by the script
* Sit back and relax while the script does all the hard work for you
* ???
* PROFIT!!
