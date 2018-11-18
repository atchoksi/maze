# Laser Maze

maze.py solves a the laser maze problem. A description of the laser maze problem is not provided because the creators do not wish it to be public.

## Running maze.py
maze.py is a command line application and can be run with the following syntax: <br>
./maze.py ./path/to/input/file ./path/to/output/file <br>
when in the folder holding maze.py <br>
IF ./maze.py command IS UNABLE TO FIND YOUR PYTHON3, YOU MUST EDIT THE FIRST LINE (THE SHEBANG LINE) TO POINT TO YOUR PYTHON3 <br>
maze.py was written with the least amount of dependencies as possible for simplicity

## Other files
-Toy_problem.ipynb is a jupyter notebook where all of the functions and classes were originally written and unit tested <br>
-classArena.py holds the class Arena <br>
-classLaser.py holds the class Laser <br>
-givenTest.txt is an example input <br>
-maze.py is the command line application <br>
-testing.txt is an example output <br>
-TestingMaze folder with all tests

## Testing
The command line application was tested in the jupyter notebook creatingInpuyFile.ipynb. Two situations were tested. <br>
One was different grid sizes with a counterclockwise laser movement. The player starts in the upper left. <br>
The laser bounces on the upper right, bottom right, and ends at coordinate (0,0). <br>
The second test was infinite loops.
