# Lists Ex1
# ----------
#
# a. Create a list with five strings
#
# b. Use append to add two strings to the list
#
# c. Use pop to remove the first element
#
# d. Find the length of the list
#
# e. Sort the list
#
# f. Access index-0 (my_list[0]) and assign it a new value.

from rich import print

my_list = ["string1", "something else", "whatever", "hello", "new"]

my_list.append("john")
my_list.append("doe")
my_list.pop(0)
my_list.sort()

my_list[0] = "new string"

print(my_list)
print(f"The length of our list is: {len(my_list)}")
