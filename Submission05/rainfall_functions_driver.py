# rainfall_functions_driver.py
# Instructor-supplied driver for the rainfall_functions module.

import sys
import rainfall_functions


def main():
    """
    The main driver function for the functions in the module
    rainfall_functions.py.
    """
    if len(sys.argv) == 1:
        rainfall_functions.display_opening_screen()
        rainfall_functions.display_program_info()
        sys.exit()

    f = open(sys.argv[1])
    rainfall_functions.process_rainfall_file(f)
    f.close()
    print("\nOK ... Program now terminating.")
    input("Press Enter to continue ... ")

main()
