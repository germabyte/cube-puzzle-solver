Cube Puzzle Solver
==================

Description
-----------

This script is a simple GUI application that helps you solve the following puzzle:

1. There are 10 cubes with 4 faces each.
2. The goal of the puzzle is to turn the cubes arranged in the column so that the sum 555 is formed on all sides.
3. Each column shows a single side of each of the 10 vertically arranged cubes.

Getting Started
---------------

To run the script, you will need Python and the `tkinter` library installed on your system. Simply run the script using a Python interpreter, and the GUI will appear.

Usage
-----

Upon starting the application, you will see the current configuration of the cubes and the sums of each column. You can manually rotate each cube by clicking the "Rotate" button next to it.

To shuffle the cubes, click the "Shuffle" button. This will randomly rotate the faces of each cube, allowing you to start with a new configuration.

To solve the puzzle, click the "Solve" button. The script will try all possible combinations of rotations to find a solution where the sum of all columns is 555. If a solution is found, the cubes will be updated to display the solution.

To find and save all possible solutions, click the "Find All Solutions" button. The script will write all solutions to a text file named "solutions.txt".

Technical Details
-----------------

The script uses the `tkinter` library to create a GUI for displaying the cubes and interacting with the user. The `itertools` library is used to generate all possible combinations of rotations for the cubes.

The `rotate` function rotates a cube by a given number of positions. The `rotate_cube` function is used to manually rotate a cube when the user clicks the "Rotate" button.

The `shuffle_cubes` function randomly rotates each cube to generate a new starting configuration.

The `is_solution` function checks if the current configuration of the cubes meets the target sum.

The `solve_cubes` function tries all possible combinations of rotations to find a solution where the sum of all columns is equal to the target sum.

The `find_all_solutions` function finds and saves all possible solutions to a text file.

The `update_cube_display` function updates the GUI with the current state of the cubes and the sums.
