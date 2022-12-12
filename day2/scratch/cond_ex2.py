# Conditionals Ex2
# ================
#
# 1. Create a variable named os_version with the following value:
#
# os_version = "15.4(2)T1"
#
# 2. Using the .split() method, extract the major version 15 and
# the minor version 4. Note, you potentially will have to use split()
# twice to extract the minor version.
#
# 3. Check if the major version is version 16 or greater. Print a message if
# this is True.
#
# 4. If that fails (i.e. major version is less than 16), then check if
# the major version is 15, and the minor version is 2 or greater (i.e. 15.2
# or greater). Print a message if this is True.
#
# 5. If neither of these conditions are true, print a message indicating that the
# os_version is invalid.
#
# /* Note, you will likely need to cast the string as integers using int(my_var) */

os_version = "15.4(2)T1"
major_version, minor_version_str = os_version.split(".")
minor_version, _ = minor_version_str.split("(")

major_version = int(major_version)
minor_version = int(minor_version)

if major_version >= 16:
    print("Major version 16.x or greater")
elif major_version == 15 and minor_version >= 2:
    print("Version 15.x where x is 2 or more")
else:
    print(f"OS version is invalid: {major_version} {minor_version}")
