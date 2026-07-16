from src.dicts import (
    merge_dicts,
    invert_dict,
    group_by_age,
    filter_by_age,
    count_by_status,
)


def test_merge_dicts_basic() -> None:
    left = {"a": 1, "b": 2}
    right = {"c": 3, "d": 4}
    expected = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_empty_left() -> None:
    left = {}
    right = {"b": 3, "c": 4}
    expected = {"b": 3, "c": 4}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_empty_right() -> None:
    left = {"a": 1, "b": 2}
    right = {}
    expected = {"a": 1, "b": 2}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_both_empty() -> None:
    left = {}
    right = {}
    expected = {}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_overlapping_keys() -> None:
    left = {"a": 1, "b": 2}
    right = {"b": 3, "c": 4}
    expected = {"a": 1, "b": 3, "c": 4}
    assert merge_dicts(left, right) == expected


def test_invert_dict_basic() -> None:
    data = {"a": "1", "b": "2", "c": "3"}
    expected = {"1": "a", "2": "b", "3": "c"}
    assert invert_dict(data) == expected


def test_invert_dict_empty() -> None:
    assert invert_dict({}) == {}


def test_invert_dict_single_item() -> None:
    data = {"a": "1"}
    expected = {"1": "a"}
    assert invert_dict(data) == expected


def test_invert_dict_duplicate_values() -> None:
    data = {"a": "1", "b": "1", "c": "2"}
    expected = {"1": "b", "2": "c"}
    assert invert_dict(data) == expected


def test_group_by_age_basic() -> None:
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 30},
    ]
    expected = {
        30: [{"name": "Alice", "age": 30}, {"name": "Charlie", "age": 30}],
        25: [{"name": "Bob", "age": 25}],
    }
    assert group_by_age(users) == expected


def test_group_by_age_empty() -> None:
    assert group_by_age([]) == {}


def test_group_by_age_missing_age() -> None:
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},
        {"name": "Charlie", "age": 30},
    ]
    expected = {
        30: [{"name": "Alice", "age": 30}, {"name": "Charlie", "age": 30}],
    }
    assert group_by_age(users) == expected


def test_group_by_age_all_missing() -> None:
    users = [
        {"name": "Alice"},
        {"name": "Bob"},
        {"name": "Charlie"},
    ]
    expected = {}
    assert group_by_age(users) == expected


def test_group_by_age_varied() -> None:
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 30},
        {"name": "David", "age": 25},
        {"name": "Eve", "age": 35},
    ]
    expected = {
        30: [{"name": "Alice", "age": 30}, {"name": "Charlie", "age": 30}],
        25: [{"name": "Bob", "age": 25}, {"name": "David", "age": 25}],
        35: [{"name": "Eve", "age": 35}],
    }
    assert group_by_age(users) == expected


def test_filter_by_age_basic() -> None:
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
    min_age = 30
    expected = [
        {"name": "Alice", "age": 30},
        {"name": "Charlie", "age": 35},
    ]
    assert filter_by_age(users, min_age) == expected


def test_filter_by_age_empty() -> None:
    assert filter_by_age([], 30) == []


def test_filter_by_age_all_below() -> None:
    users = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 25},
    ]
    min_age = 30
    expected = []
    assert filter_by_age(users, min_age) == expected


def test_filter_by_age_all_above() -> None:
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 35},
    ]
    min_age = 25
    expected = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 35},
    ]
    assert filter_by_age(users, min_age) == expected


def test_filter_by_age_missing_age() -> None:
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},
        {"name": "Charlie", "age": 35},
    ]
    min_age = 30
    expected = [
        {"name": "Alice", "age": 30},
        {"name": "Charlie", "age": 35},
    ]
    assert filter_by_age(users, min_age) == expected


def test_count_by_status_basic() -> None:
    items = [
        {"id": 1, "status": "active"},
        {"id": 2, "status": "inactive"},
        {"id": 3, "status": "active"},
    ]
    expected = {"active": 2, "inactive": 1}
    assert count_by_status(items) == expected


def test_count_by_status_empty() -> None:
    assert count_by_status([]) == {}


def test_count_by_status_missing_status() -> None:
    items = [
        {"id": 1, "status": "active"},
        {"id": 2},
        {"id": 3, "status": "active"},
    ]
    expected = {"active": 2}
    assert count_by_status(items) == expected


def test_count_by_status_all_missing() -> None:
    items = [
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ]
    expected = {}
    assert count_by_status(items) == expected
