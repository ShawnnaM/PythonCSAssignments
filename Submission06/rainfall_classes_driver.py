# rainfall_classes_driver.py
# Instructor-supplied driver for the RainfallInfo module
# and the RainfallProcessor module.

import sys
import RainfallInfo
import RainfallProcessor


def main():
    """
    The main "driver" function for the classes version of the rainfall program.

    Display an opening screen with programmer and program identification
    if no command-line arguments. Otherwise, a single command-line input is
    expected, which must be a properly formatted textfile containing monthly
    rainfall data for any number of years. The driver calls both of the
    methods in the RainfallInfo class of module RainfallInfo if there are no
    command-line inputs; otherwise a single public method of the class
    RainfallProcessor class of module RainfallProcessor is called to process
    the data in the file whose name has been entered on the command line.

    Parameters
    ----------
    sys.argv : list of str
        The list of command-line inputs, if any (at most one in this program)
    """
    if len(sys.argv) == 1:
        r_info = RainfallInfo.RainfallInfo()
        r_info.display_opening_screen()
        r_info.display_program_info()
        sys.exit()

    rainfall_file = sys.argv[1]
    rp = RainfallProcessor.RainfallProcessor(rainfall_file)
    rp.process_rainfall_file()
    print("\nOK ... Program now terminating.")
    input("Press Enter to continue ... ")

if __name__ == '__main__':
    main()
