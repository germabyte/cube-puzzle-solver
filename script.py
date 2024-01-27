import tkinter as tk
from itertools import product
import random

# Hardcoded initial configuration of cubes from the provided image
cubes = [
    [60, 95, 30, 25],
    [55, 25, 20, 70],
    [55, 10, 20, 50],
    [55, 65, 15, 45],
    [55, 90, 80, 90],
    [55, 60, 90, 85],
    [55, 45, 95, 15],
    [55, 55, 75, 65],
    [55, 55, 70, 35],
    [55, 55, 60, 75],
]

# Function to rotate a cube
def rotate(cube, n):
    return cube[n:] + cube[:n]

# Function for manually rotating a cube
def rotate_cube(i):
    cubes[i] = rotate(cubes[i], 1)
    update_cube_display()

# Function to shuffle cubes
def shuffle_cubes():
    for i in range(len(cubes)):
        shift_amount = random.randint(0, 3)
        cubes[i] = rotate(cubes[i], shift_amount)
    update_cube_display()

# Function to check if the current configuration meets a target sum
def is_solution(target_sum):
    for col in range(4):
        if sum(cubes[row][col] for row in range(len(cubes))) != target_sum:
            return False
    return True

# Function to try all combinations of rotations to find a solution
def solve_cubes(target_sum):
    for rotations in product(range(4), repeat=len(cubes)):
        for i, rot in enumerate(rotations):
            cubes[i] = rotate(cubes[i], rot)
        if is_solution(target_sum):
            update_cube_display()
            return
    update_cube_display()

# Function to update the GUI with the current state of the cubes and the sums
def update_cube_display():
    for i, cube in enumerate(cubes):
        for j, face in enumerate(cube):
            cube_labels[i][j].config(text=str(face))
    # Update the sums
    for col in range(4):
        sum_labels[col].config(text=str(sum(cubes[row][col] for row in range(len(cubes)))))

# Creating the main window
window = tk.Tk()
window.title("Cube Puzzle Solver")

# Creating labels to display the cubes
cube_labels = [[tk.Label(window, text=str(cubes[i][j]), width=10, height=2, borderwidth=2, relief="ridge") for j in range(4)] for i in range(len(cubes))]
rotate_buttons = []

for i in range(len(cubes)):
    # Rotation button for each cube
    rotate_button = tk.Button(window, text=f"Rotate {i+1}", command=lambda i=i: rotate_cube(i))
    rotate_button.grid(row=i, column=5)
    rotate_buttons.append(rotate_button)

    for j in range(4):
        cube_labels[i][j].grid(row=i, column=j)

# Labels to display the sums of each column
sum_labels = [tk.Label(window, text=str(sum(cubes[row][col] for row in range(len(cubes)))), width=10, height=2, borderwidth=2, relief="groove") for col in range(4)]
for col in range(4):
    sum_labels[col].grid(row=len(cubes), column=col)

# Function to find and write all solutions to a text file
def find_all_solutions(target_sum):
    solutions = []
    for rotations in product(range(4), repeat=len(cubes)):
        for i, rot in enumerate(rotations):
            cubes[i] = rotate(cubes[i], rot)
        if is_solution(target_sum):
            solutions.append([cube[:] for cube in cubes])
        # Reset the rotation
        for i in range(len(cubes)):
            cubes[i] = rotate(cubes[i], -rotations[i])

    # Writing solutions to a file
    with open('solutions.txt', 'w') as file:
        for idx, solution in enumerate(solutions, start=1):
            file.write(f'Solution {idx}:\n\n')
            for row_num, row in enumerate(solution, start=1):
                file.write('\t'.join(map(str, row)) + ' ' + str(row_num) + ' row\n')
            file.write('\t'.join(['555']*4) + ' sum row\n\n')
    print(f"{len(solutions)} solutions written to 'solutions.txt'")


# Buttons for shuffling and solving the puzzle
shuffle_button = tk.Button(window, text="Shuffle", command=shuffle_cubes)
shuffle_button.grid(row=len(cubes) + 1, columnspan=2)

solve_button = tk.Button(window, text="Solve", command=lambda: solve_cubes(555))  # Updated target sum is 555
solve_button.grid(row=len(cubes) + 1, column=2, columnspan=2)

# Button for finding and saving all solutions
find_solutions_button = tk.Button(window, text="Find All Solutions", command=lambda: find_all_solutions(555))
find_solutions_button.grid(row=len(cubes) + 2, columnspan=4)


# Run the application
window.mainloop()
