from python_package import module


def test_top_n():
    """
        make sure top_n works correctly
    """

    assert module.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 3], 'incorrect'
