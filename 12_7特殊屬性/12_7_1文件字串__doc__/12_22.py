# ch_12_22.py Apply file annotations to functions
def getMax(x, y):
    """
    document string example
    It is recommended that x and y be integers
    this function return big value
    """

    if int(x) > int(y):
        return x
    else:
        return y


print(getMax(2, 3))
print(getMax.__doc__)
