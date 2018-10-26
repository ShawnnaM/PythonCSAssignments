# unique_names_in_order.py

from sys import argv

print("Programmed by SM")
a_list = []
for i in range(1, len(argv)):
    a_list.append(argv[i])
changed_list = set(a_list)
changed_list2 = list(changed_list)
changed_list2.sort()
for name in changed_list2:
    print(name)
