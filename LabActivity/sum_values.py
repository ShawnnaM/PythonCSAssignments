# sum_values.py

import sys

print()
print("Programmed by SM")

sum = 0
for i in range(1, len(sys.argv)):
    sum = sum + sys.argv[i]

    print("The sum is {}.".format(sum))

input ("Press ENTER to continue ... ")