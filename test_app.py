from app import add, health_check


def test_add():
    assert add(2, 3) == 6


def test_health_check():
    assert health_check() == {"status": "ok"}
