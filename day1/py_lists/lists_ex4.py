from rich import print

print()
my_list = list(range(1, 50))
my_list = my_list + ["hello", "world"]
my_list[0] = "whatever"
print(my_list)

# -3 will be included
last_three = my_list[-3:]
print(f"Last three elements: {last_three}")

# index-7 will be excluded, but we start at zero (so that is the eighth element)
first_seven = my_list[:7]
print(f"The first seven elements: {first_seven}")
print()
