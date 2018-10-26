# converter.py
# Submission02
# Converting Time or Temperature

from sys import argv


information1 = """









                
                Submission 02
                Converting Time or Temperature












"""
"""
Program assessment:
Both converter.py and my_tests.bat programs run according to specifications.
"""

information2 = """

This program allows the user to convert either a temperature value (either
Fahrenheit to Celsius or vice versa) or a time value given as a total number
of seconds to the corresponding equivalent hours, minutes and seconds.

Input for the program is entered on the command line, and must be entered in
the following way:

The first input parameter must be one of the following:
time - to indicate that the next input will be a number of seconds
ftemp - to indicate that the next input will be a Fahrenheit temperature
ctemp - to indicate that the next input will be a Celsius temperature

The number of seconds entered must be a positive integer, but a temperature
of either kind can be a real number. The program performs the appropriate
conversion, depending on the input data, and outputs the value entered as
well as the converted equivalent.

For any conversion to take place there must be exactly two input values, the
first of which must be one of the three given above. If the number of inputs
is not two, or if the first is not one of the required ones, an appropriate
message is output and the program terminates. No error checking is performed
on the second input value, which must be an appropriate numerical value.
"""


if len(argv) == 1:
    print(information1)
    input("Press Enter to continue ... ")
    print(information2)
    input("Press Enter to continue ... ")
    exit(0)
else:
    if len(argv) != 3:
        print("Error: Incorrect number of input values (must be exactly 2).")
        print("Program now terminating.")
        exit(0)
    elif argv[1] == "ctemp":
        ce = float(argv[2])
        fa = (ce * (9/5)) + 32
        print("{:2.2f} degrees Celsius is equivalent to"
              " {:2.2f} degrees Fahrenheit.".format(ce, fa))
    elif argv[1] == "ftemp":
        fa = float(argv[2])
        ce = (fa - 32) * (5/9)
        print("{:2.2f} degrees Fahrenheit is equivalent to"
              " {:2.2f} degrees Celsius.".format(fa, ce))
    elif argv[1] == "time":
        t = int(argv[2])
        seconds = t % 60
        mins = t // 60
        minutes = mins % 60
        hours = mins // 60
        print("{} seconds in hh:mm:ss format is"
              " {:02d}:{:02d}:{:02d}.".format(t, hours, minutes, seconds))
    else:
        print("Error: Bad first parameter.")
        print("Program now terminating.")
        exit(0)
