import re

with open("aruba_show_version.txt") as f:
    data = f.read()

match = re.search(r"MODEL: (\d+).* Version (\S+)", data)
if match:
    model = match.group(1)
    os_version = match.group(2)

match = re.search(r"AP uptime is (.*)$", data, flags=re.M)
if match:
    uptime = match.group(1)

print()
print(f"Model: {model}")
print(f"OS Version: {os_version}")
print(f"Uptime: {uptime}")
print()
