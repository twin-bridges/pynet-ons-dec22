# 1. Create a function that has four parameters named var1, var2, var3, var4.
#
# 2. In the function print out each variable and indicate which variable it is.
#
# 3. Call the function using entirely positional arguments.
#
# 4. Call the function using entirely named arguments.
#
# 5. Call the function with var1 as a positional argument and var2 through var4 as named
# arguments.
#
# 6. Try to call the function with var1 specified first and using a named argument (and
# var2 through var4 as positional arguments, but specified after var1). This will generate
# an error.


def some_func(var1, var2=2, var3=3, var4=4):
    print(f"Var1: {var1}")
    print(f"Var2: {var2}")
    print(f"Var3: {var3}")
    print(f"Var4: {var4}")

    # return var1 + var2 + var3 + var4


def my_func(var1, var2):
    if my_list is None:
        my_list = []


my_list = [22, 33, "hello"]
some_func(my_list, var4=800)
