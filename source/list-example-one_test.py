import importlib

module = importlib.import_module("list-example-one")


def test_skip_elements_with_list_of_chars():
    testcase_input = ["a", "b", "c", "d", "e", "f", "g"]
    expected_output = ["a", "c", "e", "g"]
    assert module.skip_elements(testcase_input) == expected_output


def test_skip_elements_with_list_of_words():
    testcase_input = ["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"]
    expected_output = ["Orange", "Strawberry", "Peach"]
    assert module.skip_elements(testcase_input) == expected_output


def test_skip_elements_with_empty_list():
    testcase_input = []
    expected_output = []
    assert module.skip_elements(testcase_input) == expected_output
