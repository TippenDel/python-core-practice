import pytest

from src.collections_utils import flatten, unique_preserve_order, chunk_list


def test_flatten():
    assert flatten([1, 2, [3, 4], [5, [6, 7]], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert flatten([]) == []
    assert flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]
    assert flatten([[1], [2], [3], [4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[[[[[1]]]]]]) == [1]


def test_unique_preserve_order():
    assert unique_preserve_order([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    assert unique_preserve_order([]) == []
    assert unique_preserve_order([1, 1, 1, 1]) == [1]
    assert unique_preserve_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert unique_preserve_order([1, "1", 2, "2", 1]) == [1, "1", 2, "2"]


def test_chunk_list():
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3, 4], 1) == [[1], [2], [3], [4]]
    assert chunk_list([], 3) == []
    assert chunk_list([1, 2, 3], 10) == [[1, 2, 3]]
    assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]
    assert chunk_list([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], 0)
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], -1)
