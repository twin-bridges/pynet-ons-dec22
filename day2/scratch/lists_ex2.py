#
#Lists Ex2
#----------
#
#a. Create two lists named list1 and list2 containing various strings, integers,
#   and floats.
#
#b. Create a list3 by concatenating list1 and list2 together.
#
#c. Use rich.print to print out this list3.
#
#d. Instead of using list concatenation now directly modify list1 by using 
#   list1.extend(list2)
#
#e. Pop off the very first element of list3 and save it to a variable named 
#   first_element. Print out this variable. Also verify list3 has changed 
#   (i.e. no longer has the first element).
from rich import print

my_list1 = [22, 3.14, "hello"]
my_list2 = ["some string", 2, 17.8, "whatever"]

my_list3 = my_list1 + my_list2
# print(my_list3)

my_list1.extend(my_list2)
# print(my_list1)

first_element = my_list3.pop(0)
print(first_element)

print(my_list3)
