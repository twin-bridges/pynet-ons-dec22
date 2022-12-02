os_version = "15.4(2)T1"

ver_major, ver_minor_other = os_version.split(".")
ver_minor = ver_minor_other.split("(")[0]

ver_major = int(ver_major)
ver_minor = int(ver_minor)
print()
print(ver_major)
print(ver_minor)

if ver_major >= 16:
    print("\nMajor Version is at least version\n")
elif ver_major == 15 and ver_minor >= 3:
    print("\nMajor Version 15, Minor Version >= 3\n")
else:
    print("\nOS Version is invalid.\n") 