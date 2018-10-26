# rainfall_functions.py
# Submission05
# Retrieving and Processing Rainfall Data
"""
Program assessment:
The rainfall_functions.py program runs according to specifications with the
provided rainfall_functions_driver.py program.
"""

import os


def display_opening_screen():
    """ Display's the opening screen with user and submission information. """

    print("""









                
                Submission 05
                Retrieving and Processing Rainfall Data












""")
    input("Press Enter to continue ... ")


def display_program_info():
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


def read_in_file(f):
    """" This function reads in the file and takes the rainfall data
         and puts it into a tuple. """
    rain_data = {}
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            rain_data[line] = tuple(f.readline().split())
        else:
            break
    return rain_data


def get_and_print_data(rain_data):
    """ This function checks to see that the user's answer was not no and
        then asks for a year to get data on to which it then display's in a
        table. """
    answer = ""
    while answer != "n":
        os.system("cls")
        year = input("Enter year for which you want rainfall data: ")
        print_rainfall_data(rain_data, year)
        input("Press Enter to continue ... ")
        print("")
        answer = input("Do it again for another year? [[y]/n] ")


def print_rainfall_data(rain_data, year):
    """" This function takes the year inputted by the user and creates
         a data table of rainfall amounts with the corresponding month as
         well as rainfall information such as the total, the average, and
         the month with the most and least rainfall. """
    print("")
    if year in rain_data:
        rain = rain_data.get(year)
        print("===== Rainfall Summary for {}".format(year))
        print("January.....{:>5.1f}   July........"
              "{:>5.1f}".format(float(rain[0]), float(rain[6])))
        print("February....{:>5.1f}   August......"
              "{:>5.1f}".format(float(rain[1]), float(rain[7])))
        print("March.......{:>5.1f}   September..."
              "{:>5.1f}".format(float(rain[2]), float(rain[8])))
        print("April.......{:>5.1f}   October....."
              "{:>5.1f}".format(float(rain[3]), float(rain[9])))
        print("May.........{:>5.1f}   November...."
              "{:>5.1f}".format(float(rain[4]), float(rain[10])))
        print("June........{:>5.1f}   December...."
              "{:>5.1f}".format(float(rain[5]), float(rain[11])))
        total = total_rainfall(rain)
        ave = average_rainfall(total)
        max_month = max_rain_month(rain)
        min_month = min_rain_month(rain)
        print("===== Total rainfall for the year... {0:.1f}".format(total))
        print("===== Average monthly rainfall...... {0:.1f}".format(ave))
        print("===== Month with highest rainfall... {}".format(max_month))
        print("===== Month with lowest rainfall.... {}".format(min_month))
    else:
        print("No rainfall data found for year {}.".format(year))


def total_rainfall(rain):
    """ This function finds the total rainfall amount by summing the values
        of the year entered by the user to return a float. """
    total = 0
    for i in range(len(rain)):
        total += float(rain[i])
    return total


def average_rainfall(total):
    """ This function finds the average rainfall amount by taking the total
        rainfall and dividing it by the number of months to return a float. """
    return total / 12


def max_rain_month(rain):
    """ This function finds the month with the largest rainfall amount and
        returns the month name (i.e. a string) at which this occurs. """
    months = ['January', 'February', 'March', 'April',
              'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    max_rain = rain.index(max(rain, key=float))
    return months[max_rain]


def min_rain_month(rain):
    """ This function finds the month with the lowest rainfall amount and
        returns the month name (i.e. a string) at which this occurs. """
    months = ['January', 'February', 'March', 'April',
              'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    min_rain = rain.index(min(rain, key=float))
    return months[min_rain]


def process_rainfall_file(f):
    """ This function reads in a text file entered by the user and prompts
        the user to enter a year for which they'd like rainfall data on. """
    rain_call = read_in_file(f)
    get_and_print_data(rain_call)
