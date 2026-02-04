from app import format_currency

def test_format_currency_two_decimals():
    assert format_currency(10.126) == 10.13


from app import add


def test_add():
    assert add(2, 3) == 5

