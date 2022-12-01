#!/usr/bin/env python
from rich import print

print()
list1 = [22, "hello", "whatever", 4.2]
list2 = ["Some", "thing", 18, 9.1]

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

first_element = list3.pop(0)
print(first_element)
print(list3)
print()
