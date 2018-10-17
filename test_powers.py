import powers

def test_squares():
    assert powers.list_powers(3, 2) == [1, 4, 9]

def test_cubes():
    assert powers.list_powers(3, 3) == [1, 8, 27]

