def list_powers(n, m):
    """
    returns a list of squares

    >>> list_powers(3, 2)
    [1, 4, 9]
    >>> list_powers(3, 3)
    [1, 8, 27]
    """
    assert n > 0
    li = [] 
    for i in range(1, n+1):
        li.append(i**m)
    return li

if __name__ == "__main__":
    import sys
    try:
        number_of_elements = int(sys.argv[1])
        exponent = int(sys.argv[2])
    except IndexError:
        print(f"Usage: {sys.argv[0]} number_of_elements exponent")
        sys.exit(1)

    for i in list_powers(number_of_elements, exponent):
        print(i)
