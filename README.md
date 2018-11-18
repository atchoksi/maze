This is a command line application that solves the simple laser maze problem.
I am not describing the problem explicitly because the creators do not want it to be shared.

Run the command line application as follows:
./maze.py ./path/to/input/file ./path/to/output/file
argument0 - maze.py python script that holds the algorithm to solve laser maze problem. maze.py calls python in the first shebang line.
IF THERE ARE PROBLEMS RUNNING PYTHON, EDIT THE SHEBANG LINE TO POINT TO YOUR PYTHON3.
argument1 - path to input file
argument2 - path to output file

Other files in the repository are:
-Toy_problem.ipynb which is a jupyter notebook in which all functions and classes were built and unit tested
-classArena.py script that holds class Arena
-classLaser.py script that holds class Laser
-givenTest.txt sample input
-testing.txt sample output

Testing:
-RandomInput - 10 randomly generated mazes and a script to generate random mazes
-RandomOutput - random mazes solved
-InfiniteLoopInput - 2 infinite loop mazes
-InfiniteLoopOutput - output to 2 infinite loop mazes
