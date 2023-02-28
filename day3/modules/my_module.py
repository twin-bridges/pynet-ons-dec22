#
# In a new Python file do the following.
#
# Create a function that takes a number as input and returns the number squared.
#
# Create a second function that takes two numbers and returns the product of those
# numbers.
#
# Use the "if __name__ == "__main__":" technique and separate the functions from the
# executable code.
#
# For the executable code, test your two functions using a couple of test cases. You can use
# assert statements to verify your test cases work.
#
# For example, as a simple test you can do something like the following:
#
#    result = squared(2)
#    assert result == 4
#
# Introduce a simple error in your testing (i.e. something that results in the test statements being
# False) and observe that your testing catches this error.


def exponent(x):
    return x**2


def product(y, z):
    return y * z


if __name__ == "__main__":
    print("Hello world")

    res = exponent(2)
    assert res == 4
