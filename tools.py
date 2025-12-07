import os
import subprocess

def create_advent_files():
    """
    Asks for a day number and creates the corresponding dayXX.py
    and inputX.txt files in the current directory.
    """
    try:
        folder_name = "2025"
        day_input = input("Enter the Advent of Code day number (e.g., 5): ")
        day_num = int(day_input)

        if not 1 <= day_num <= 25:
            print("Error: Please enter a day between 1 and 25.")
            return


        day_str_padded = f"{day_num:02d}"
        py_filename = os.path.join(folder_name,f"day{day_str_padded}.py")
        txt_filename = os.path.join(folder_name,f"input{day_num}.txt")
        input_filename = f"input{day_num}.txt"

        #  some boilerplate code for the Python file
        py_boilerplate = f'''


def part1():
    with open("{input_filename}", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line)

def part2():
    with open("{input_filename}", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line)


print("--- Part 1 ---")
part1()

# print("\\n--- Part 2 ---")
# part2()
'''

        if os.path.exists(py_filename) or os.path.exists(txt_filename):
            print(f"Error: '{py_filename}' or '{txt_filename}' already exist.")
            return


        with open(py_filename, "w") as py_file:
            py_file.write(py_boilerplate.strip())

        with open(txt_filename, "w") as txt_file:
            pass

        print(f"Successfully created '{py_filename}'")
        print(f"Successfully created '{txt_filename}'")
        subprocess.run(["git", "add", py_filename], check=True, capture_output=True)
        print(f"-> Staged '{py_filename}' for commit.")

        subprocess.run(["git", "add", txt_filename], check=True, capture_output=True)

    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    create_advent_files()