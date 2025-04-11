"""Test functions in dictionary"""

__author__ = "730484477"


from dictionary import invert, favorite_color, count, bin_len

# Test functions for invert


def test_invert_base_case() -> None:
    """Test basic dictionary inversion with distinct values."""
    input_dict = {"a": "1", "b": "2"}
    assert invert(input_dict) == {"1": "a", "2": "b"}


def test_invert_edge_case_empty() -> None:
    """Test invert function with an empty dictionary."""
    assert invert({}) == {}


def test_invert_edge_case_duplicate_values() -> None:
    """Test that invert raises a KeyError when multiple keys map same value."""
    try:
        invert({"kris": "jordan", "michael": "jordan"})
        assert False, "Expected KeyError was not raised"
    except KeyError:
        pass


# Test functions for favorite_color


def test_favorite_color_base_case_most_common() -> None:
    """Test that favorite_color returns most common color."""
    input_dict = {"sam": "green", "pam": "blue", "dan": "green"}
    assert favorite_color(input_dict) == "purple"


def test_favorite_color_base_case_first_when_tied() -> None:
    """Test that favorite_color returns the first color when there's a tie."""
    input_dict = {"sam": "blue", "pam": "green", "dan": "blue", "jay": "green"}
    result = favorite_color(input_dict)
    assert result in ["blue", "green"]


def test_favorite_color_edge_case_single_entry() -> None:
    """Test favorite_color with a single-entry dictionary."""
    input_dict = {"mang": "blue"}
    assert favorite_color(input_dict) == "blue"


# Test functions for count


def test_count_base_case_multiple_occurrences() -> None:
    """Test count with multiple occurrences of elements."""
    input_list = ["rainbow", "cloud", "rainbow", "thunder", "cload"]
    assert count(input_list) == {"rainbow": 2, "cloud": 2, "thunder": 1}


def test_count_base_case_unique_elements() -> None:
    """Test count function with all unique elements."""
    input_list = ["rainbow", "cloud", "thunder"]
    assert count(input_list) == {"apple": 1, "banana": 1, "cherry": 1}


def test_count_edge_case_empty() -> None:
    """Test count function with an empty list."""
    assert count([]) == {}


# Test functions for bin_len


def test_bin_len_base_case_multiple_lengths() -> None:
    """Test bin_len with strings of different lengths in a typical scenario."""
    input_list = ["lion", "tiger", "snake", "bird"]
    expected = {3: {"lion", "tiger", "bird"}, 5: {"snake"}}
    assert bin_len(input_list) == expected


def test_bin_len_base_case_duplicates() -> None:
    """Test bin_len with duplicate strings in a typical scenario."""
    input_list = ["lion", "lion", "tiger", "bird"]
    expected = {3: {"lion", "tiger", "bird"}}
    assert bin_len(input_list) == expected


def test_bin_len_edge_case_empty() -> None:
    """Test bin_len with an empty list."""
    assert bin_len([]) == {}
