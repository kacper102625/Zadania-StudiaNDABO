from calculator import calculate_expression

def test_calculate_expression():
    result = calculate_expression()
    assert result == 6.0  # (((10 + 5) - 3) * 2) / 4 = 6.0
