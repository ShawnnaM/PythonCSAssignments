# max_min_values.py

from sys import argv

print("Programmed by SM")
if len(argv) == 1:
    print("Warning: You must enter at least one number on the command line.")
    input("Press Enter to continue ... ")
else:
    max_value = float(argv[1])
    min_value = float(argv[1])
    max_index = 1
    min_index = 1
    for i in range(1, len(argv)):
        if float(argv[i]) > float(max_value):
            max_value = (argv[i])
            max_index = i
        if float(argv[i]) < float(min_value):
            min_value = (argv[i])
            min_index = i
    print("The largest value input was {}, "
          "which occured at position {}.".format(argv[max_index], max_index))
    print("The smallest value input was {}, "
          "which occured at position {}.".format(argv[min_index], min_index))
    input("Press Enter to continue ... ")

