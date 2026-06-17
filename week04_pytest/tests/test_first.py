def test_addition():
    result = 2 + 2
    assert result == 4     # ← намеренно сломали


def test_string_concatenation():
    greeting = "Hello, " + "World!"
    assert greeting == "Hello, World!"


def test_list_length():
    items = [1, 2, 3, 4, 5]
    assert len(items) == 5