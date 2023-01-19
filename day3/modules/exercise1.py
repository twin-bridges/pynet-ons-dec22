def squared(x):
    return x**2


def product(x, y):
    return x * y


if __name__ == "__main__":

    print("TEST CODE SECTION")
    result = squared(2)
    assert result == 4

    result = squared(-1)
    assert result == 1

    result = product(2, 10)
    assert result == 20
