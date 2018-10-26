# RainfallProcessor.py
# Submission06
# Retrieving and Processing Rainfall Data
"""
Program assessment:
The RainfallProcessor.py program runs according to specifications with the
rainfall_classes_driver.py program.
"""
import os


class RainfallProcessor:
    def __init__(self, rainfall_input_file):
        """ This function is a class "constructor" for the program. """
        self._rainfall_file = rainfall_input_file

    def read_in_file(self):
        """" This function reads in the file and takes the rainfall data
             and puts it into a tuple. """
        f = open(self._rainfall_file)
        rain_data = {}
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                rain_data[line] = tuple(f.readline().split())
            else:
                break
        f.close()
        return rain_data

    def process_rainfall_file(self):
        """ This function reads in a text file entered by the user and prompts
            the user to enter a year for which they'd like rainfall data on."""
        rain_call = self.read_in_file()
        self.get_and_print_data(rain_call)

    def get_and_print_data(self, rain_data):
        """ This function checks to see that the user's answer was not no and
            then asks for a year to get data on to which it then display's in a
            table. """
        answer = ""
        while answer != "n":
            os.system("cls")
            year = input("Enter year for which you want rainfall data: ")
            self.print_rainfall_data(rain_data, year)
            input("Press Enter to continue ... ")
            print("")
            answer = input("Do it again for another year? [[y]/n] ")

    def print_rainfall_data(self, rain_data, year):
        """" This function takes the year inputted by the user and creates
             a data table of rainfall amounts with the corresponding month as
             well as rainfall information. The rainfall information such as
             the total, the average rainfall amounts as well as the month
             with the most and least rainfall is then outputted to the user."""
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
            total = self.total_rainfall(rain)
            ave = self.average_rainfall(total)
            max_month = self.max_rain_month(rain)
            min_month = self.min_rain_month(rain)
            print("===== Total rainfall for the year... {0:.1f}".format(total))
            print("===== Average monthly rainfall...... {0:.1f}".format(ave))
            print("===== Month with highest rainfall... {}".format(max_month))
            print("===== Month with lowest rainfall.... {}".format(min_month))
        else:
            print("No rainfall data found for year {}.".format(year))

    def total_rainfall(self, rain):
        """ This function finds the total rainfall amount by summing the values
            of the year entered by the user to return a float. """
        total = 0
        for i in range(len(rain)):
            total += float(rain[i])
        return total

    def average_rainfall(self, total):
        """ This function finds the average rainfall amount by
            taking the total rainfall and dividing it by the
            number of months to return a float."""
        return total / 12

    def max_rain_month(self, rain):
        """ This function finds the month with the largest rainfall amount and
            returns the month name (i.e. a string) at which this occurs. """
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']
        max_rain = rain.index(max(rain, key=float))
        return months[max_rain]

    def min_rain_month(self, rain):
        """ This function finds the month with the lowest rainfall amount and
            returns the month name (i.e. a string) at which this occurs. """
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']
        min_rain = rain.index(min(rain, key=float))
        return months[min_rain]
