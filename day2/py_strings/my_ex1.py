# Read in the “aruba_show_ap_database.txt” file.

# Process the data such that all of the header and footer information is excluded.

# In other words, only print out the tabular data from the file. Your output should look as follows:

from rich import print

with open("aruba_show_ap_database.txt") as my_file:
    data = my_file.read()

print(data)
my_lines = data.splitlines()

header = True
footer = False

aruba_aps = {}

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
    # print(element)

    fields = element.split()
    ap_name = fields[0]
    ip_addr = fields[3]
    up_down_status = fields[4]

    aruba_aps[ap_name] = up_down_status
    # print(f"AP Name: {ap_name}")
    # print(ip_addr)
    # print(up_down_status)

print(aruba_aps)
