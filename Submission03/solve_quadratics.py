# solve_quadratics.py
# Submission03
# Solving Quadratic Equations
"""
Program assessment:
Both solve_quadratics.py and my_tests.bat
programs run according to specifications.
"""
from sys import argv

information1 = """









                
                Submission 03
                Solving Quadratic Equations












"""
information2 = """

This program solves quadratic equations, one equation per run, if the
equation is in fact solvable (has real roots).

If not, the program simply reports that the equation cannot be solved,
pauses, and then terminates when the user presses Enter.

The coefficients of the standard quadratic equation

ax**2 + bx + c = 0

are entered on the command line in the order a, b, c. If nothing is entered
on the command line, an opening identification screen is displayed first,
followed by a screen containing this information. Each screen has a pause at
the end to allow the user to read it.

If one or more values are entered, the program checks to make sure that
there are exactly three, and reports an error if that is not the case.
If there are three values, they are all assumed to be real numbers, and
no further error checking is performed. If the entered values do correspond
to a solvable quadratic equation, the two roots of the equation are computed
and displayed. Depending on the coefficients, the roots may, of course, be
identical. In any case, a pause again precedes program termination.

"""
if len(argv) == 1:
    print(information1)
    input("Press Enter to continue ... ")
    print(information2)
    input("Press Enter to continue ... ")
    exit(0)
elif len(argv) != 4:
    print("Error: Wrong number of command-line arguments (must be three).")
    print("Program now terminating.")
    input("Press Enter to continue ... ")
    exit(0)
a = float(argv[1])
b = float(argv[2])
c = float(argv[3])
d = b**2 - 4*a*c
equation = "{:.0f}x**2".format(a)
if a == 1:
    equation = "x**2"
elif a == -1:
    equation = "-x**2"
if b != 0:
    if b == 1:
        equation += "+x"
    elif b == -1:
        equation += "-x"
    elif b < 0:
        equation += "{:.0f}x".format(b)
    elif b > 0:
        equation += "+{:.0f}x".format(b)
if c != 0:
    if c < 0:
        equation += "{:.0f}".format(c)
    else:
        equation += "+{:.0f}".format(c)
if d > 0:
    p_root = (-b + (d**(1/2))) / (2*a)
    n_root = (-b - (d**(1/2))) / (2*a)
    if p_root == -0:
        p_root = abs(p_root)
    if n_root == -0:
        n_root = abs(n_root)
    print("The quadratic equation {} = 0 has the two roots "
          "{:0<2.2f} and {:0<2.2f}. ".format(equation, p_root, n_root))
    print("Program now terminating.")
    input("Press Enter to continue ... ")
elif d == 0:
    o_root = (-b / (2*a))
    print("The quadratic equation {} = 0 has two"
          " identical roots equal to {:0<2.2f}.".format(equation, o_root))
    print("Program now terminating.")
    input("Press Enter to continue ... ")
else:
    print("Warning: The quadratic equation {} = 0 "
          "has no roots.".format(equation))
    print("Program now terminating.")
    input("Press Enter to continue ... ")
