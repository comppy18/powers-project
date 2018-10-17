def list_powers(n, m):
    """
    returns a list of squares

    >>> list_powers(3, 2)
    [1, 4, 9]
    >>> list_powers(3, 3)
    [1, 8, 27]
    """
    li = [] 
    for i in range(1, n+1):
        li.append(i**m)
    return li

if __name__ == "__main__":
    for i in list_powers(4, 3):
        print(i)
