filename = "show_versionz.txt"

try:
    f = open(filename)
    data = f.read()
    f.close()
    print("\nFile opened successfully\n")
except FileNotFoundError:
    print("\nThe file was not found\n")
    data = ""
