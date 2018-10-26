# rainfall.py
# McGowan:Shawnna:A00393797:csc227025
# Submission04
# Retrieving and Processing Rainfall Data
"""
Program assessment:
The rainfall.py program runs according to specifications.
"""
from sys import argv
import os
information1 = """









                
                Submission 04
                Retrieving and Processing Rainfall Data












"""
information2 = """

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

"""
if len(argv) == 1:
    print(information1)
    input("Press Enter to continue ... ")
    print(information2)
    input("Press Enter to continue ... ")
    exit(0)
f = open(argv[1])
rain_data = {}
while True:
    line = f.readline()
    if line:
        line = line.strip()
        rain_data[line] = tuple(f.readline().split())
    else:
        break
answer = ""
while answer != "n":
    os.system("cls")
    year = input("Enter year for which you want rainfall data: ")
    print("")
    if year in rain_data:
        rain = rain_data.get(year)
        print("===== Rainfall Summary for {}".format(year))
        print("January.....\t{:.1f}\tJuly........\t"
              "{:.1f}".format(float(rain[0]), float(rain[6])))
        print("February....\t{:.1f}\tAugust......\t"
              "{:.1f}".format(float(rain[1]), float(rain[7])))
        print("March.......\t{:.1f}\tSeptember...\t"
              "{:.1f}".format(float(rain[2]), float(rain[8])))
        print("April.......\t{:.1f}\tOctober.....\t"
              "{:.1f}".format(float(rain[3]), float(rain[9])))
        print("May.........\t{:.1f}\tNovember....\t"
              "{:.1f}".format(float(rain[4]), float(rain[10])))
        print("June........\t{:.1f}\tDecember....\t"
              "{:.1f}".format(float(rain[5]), float(rain[11])))
        total = 0
        for i in range(len(rain)):
            total += float(rain[i])
        ave = total / 12
        months = ['January', 'February', 'March', 'April',
                  'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']
        max_rain = rain.index(max(rain, key=float))
        min_rain = rain.index(min(rain, key=float))
        max_month = months[max_rain]
        min_month = months[min_rain]
        print("===== Total rainfall for the year... {0:.1f}".format(total))
        print("===== Average monthly rainfall...... {0:.1f}".format(ave))
        print("===== Month with highest rainfall... {}".format(max_month))
        print("===== Month with lowest rainfall.... {}".format(min_month))
    else:
        print("No rainfall data found for year {}.".format(year))
    input("Press Enter to continue ... ")
    print("")
    answer = input("Do it again for another year? [[y]/n] ")
print("")
print("OK ... Program now terminating.")
input("Press Enter to continue ... ")
exit(0)
f = close(argv[1])
