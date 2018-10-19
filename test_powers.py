import powers

def test_squares():
    assert powers.list_powers(3, 2) == [1, 4, 9]

def test_cubes():
    assert powers.list_powers(3, 3) == [1, 8, 27]

def test_main():
    import sys
    sys.argv[1:3] = [3, 2]
    assert powers.main() == 0
