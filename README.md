# Laser Maze

maze.py solves a the laser maze problem. A description of the laser maze problem is not provided because the creators do not wish it to be public.

## Running maze.py
maze.py is a command line application and can be run with the following syntax: \n
./maze.py ./path/to/input/file ./path/to/output/file \n
when in the folder holding maze.py\n
IF ./maze.py command IS UNABLE TO FIND YOUR PYTHON3, YOU MUST EDIT THE FIRST LINE (THE SHEBANG LINE) TO POINT TO YOUR PYTHON3\n
maze.py was written with the least amount of dependencies as possible for simplicity

## Other files
-Toy_problem.ipynb is a jupyter notebook where all of the functions and classes were originally written and unit tested\n
-classArena.py holds the class Arena\n
-classLaser.py holds the class Laser\n
-givenTest.txt is an example input\n
-maze.py is the command line application\n
-testing.txt is an example output\n
-TestingMaze folder with all tests

## Testing
The command line application was tested in the jupyter notebook creatingInpuyFile.ipynb. Two situations were tested.\n
One was different grid sizes with a counterclockwise laser movement. The player starts in the upper left.\n
The laser bounces on the upper right, bottom right, and ends at coordinate (0,0). \n
The second test was infinite loops.
