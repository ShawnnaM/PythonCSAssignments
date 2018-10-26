# read_binary_ints.py

import pickle

print("Programmed by Shawnna McGowan")


def main():
    end_of_file = False
    input_file = open('integers.dat', 'rb')
    while not end_of_file:
        try:
            i = pickle.load(input_file)
            print(i, end=' ')

            numbers_list = []
            for num in i:
                num = num.split()
                numbers_list.append(num)
                max_value = max(numbers_list)
                min_value = min(numbers_list)
                print("\nThe maximum value is {} and the minimum value is {}.".format(max_value, min_value))
        except EOFError:
            end_of_file = True
    input_file.close()

main()
