from greeting import greet, give_and


def test_greet():
    # Given
    name = "Bob"
    expected_greeting = "Hello, Bob."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_no_name():
    # Given
    name = None
    expected_greeting = "Hello, my friend."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_all_uppercase():
    # Given
    name = "JERRY"
    expected_greeting = "HELLO JERRY!"
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_numbers():
    # Given
    name = "1234"
    expected_greeting = "Hello, robot."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_arrays():
    # Given
    name = ["Jill", "Jane"]
    expected_greeting = "Hello, Jill and Jane."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_greet_numbers_c():
    # Given
    name = "1234c"
    expected_greeting = "Hello, 1234c."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting


def test_give_and():
    # Given
    name = ["Jill", "Jane"]
    expected_out = "Jill and Jane"
    # When
    out = give_and(name)
    # Then
    assert out == expected_out


def test_greet_arrays_more_than_2():
    # Given
    name = ["Amy", "Brian", "Charlotte"]
    expected_greeting = "Hello, Amy, Brian and Charlotte."
    # When
    greeting = greet(name)
    # Then
    assert greeting == expected_greeting
