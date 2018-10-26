# pickle_ints.py
# This program demonstrates object pickling.
# The "objects" here are, however, just integers.

import pickle
import random

# main function
def main():
    # Open a file for binary writing.
    output_file = open('integers.dat', 'wb')

    # Write 10 random integers to the file.
    for i in range(10):
        pickle.dump(random.randint(1, 100), output_file);

    # Close the file.
    output_file.close()

    print('Ten random integers in 1..100 have been '
        + '\nwritten to the file integers.dat.')
    input('Press Enter to continue ... ')

main()
