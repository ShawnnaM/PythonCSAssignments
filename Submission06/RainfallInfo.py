# RainfallInfo.py
# Submission06
# Retrieving and Processing Rainfall Data
"""
Program assessment:
The RainfallInfo.py program runs according to specifications with the
rainfall_classes_driver.py program.
"""


class RainfallInfo:
    def display_opening_screen(self):
        """"Shows the opening screen with user and submission information."""

        print("""









                
                Submission 06
                Retrieving and Processing Rainfall Data












                """)
        input("Press Enter to continue ... ")

    def display_program_info(self):
        """ Display's the program's information. """

        print("""
This program opens a file of text containing rainfall data for any number of
years. The data for any year is contained on two lines of the file. The first
of those two lines contains just the year, while the second line contains 12
values, each representing the recorded rainfall for a month of the year given
on the preceding line. Thus the file data for two years might look like this:
2014
12 23.5 20 17.2 15 19 16 3 12 22 11.6 7
2015
10 18.2 10 11 7.5 1.9 5 3 9.6 13 6 5.4

Note that the rainfall amounts can be integers or real numbers and that the
values are separated by blank spaces. No units (centimetres or inches, say)
are given, since they are irrelevant for our purposes.

The name of the file containing the rainfall data must be entered as the only
command-line argument, and the file is assumed to exist and be located in the
current directory (the directory in which the program is running). If data for
the entered year exists, it is displayed along with the yearly total and the
monthly average rainfall amounts, as well as the months with the highest and
lowest rainfall amounts. If no data exists for the year entered, a message to
that effect is output. The data for any number of years may be processed on a
single run.
                """)
