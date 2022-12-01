#!/usr/bin/env python
from rich import print

print()
my_list = ["hello", "New", "something", "else", "now"]
my_list.append("whatever")
my_list.append("xyz")
print(my_list.pop(0))

print(f"Length of list: {len(my_list)}")
my_list.sort()
print(my_list)

my_list[0] = "new value"
print(my_list)
print()
