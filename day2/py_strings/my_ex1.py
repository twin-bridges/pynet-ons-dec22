# Read in the “aruba_show_ap_database.txt” file.

# Process the data such that all of the header and footer information is excluded.

# In other words, only print out the tabular data from the file. Your output should look as follows:

with open("aruba_show_ap_database.txt") as my_file:
    data = my_file.read()

my_lines = data.splitlines()

header = True
footer = False
for element in my_lines:
    if "-------" in element and "     " in element:
        header = False
        continue
    if header:
        continue
    if "Flags:" in element:
        footer = True
    if footer:
        continue
    if not element:
        continue
    print(element)
