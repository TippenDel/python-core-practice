from src.dicts import (
    merge_dicts,
    invert_dict,
    group_by_age,
    filter_by_age,
    count_by_status,
)


def test_merge_dicts():
    left = {"a": 1, "b": 2}
    right = {"c": 3, "d": 4}
    expected = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_overlapping():
    left = {"a": 1, "b": 2}
    right = {"b": 3, "c": 4}
    expected = {"a": 1, "b": 3, "c": 4}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_empty():
    assert merge_dicts({}, {}) == {}


def test_merge_dicts_nested():
    left = {"a": 1, "b": 2, "c": {"aa": 11, "bb": 22}}
    right = {"d": 3}
    expected = {"a": 1, "b": 2, "c": {"aa": 11, "bb": 22}, "d": 3}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_nested_overlapping():
    left = {"a": 1, "b": 2, "c": {"aa": 11, "bb": 22}}
    right = {"c": {"cc": 33}, "d": 3}
    expected = {"a": 1, "b": 2, "c": {"cc": 33}, "d": 3}
    assert merge_dicts(left, right) == expected


def test_merge_dicts_left_empty():
    right = {"a": 1, "b": 2}
    expected = {"a": 1, "b": 2}
    assert merge_dicts({}, right) == expected


def test_merge_dicts_right_empty():
    left = {"a": 1, "b": 2}
    expected = {"a": 1, "b": 2}
    assert merge_dicts(left, {}) == expected


def test_invert_dict():
    data = {"a": "apple", "b": "banana", "c": "cherry"}
    expected = {"apple": "a", "banana": "b", "cherry": "c"}
    assert invert_dict(data) == expected


def test_invert_dict_empty():
    assert invert_dict({}) == {}


def test_invert_dict_overlapping_values():
    data = {"a": "apple", "b": "banana", "c": "apple"}
    expected = {"apple": "c", "banana": "b"}
    assert invert_dict(data) == expected


def test_group_by_age():
    users = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 40},
        {"name": "Ivan", "age": 30},
        {"name": "Eve"},
    ]
    expected = {
        30: [{"name": "Anna", "age": 30}, {"name": "Ivan", "age": 30}],
        40: [{"name": "Bob", "age": 40}],
    }
    assert group_by_age(users) == expected


def test_group_by_age_empty():
    assert group_by_age([]) == {}


def test_group_by_age_all_missing():
    users = [{"name": "Anna"}, {"name": "Bob"}, {"name": "Ivan"}]
    assert group_by_age(users) == {}


def test_group_by_age_all_same():
    users = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 30},
        {"name": "Ivan", "age": 30},
    ]
    expected = {
        30: [
            {"name": "Anna", "age": 30},
            {"name": "Bob", "age": 30},
            {"name": "Ivan", "age": 30},
        ]
    }
    assert group_by_age(users) == expected


def test_filter_by_age():
    users = [
        {"name": "Anna", "age": 30},
        {"name": "Bob", "age": 20},
        {"name": "Ivan", "age": 25},
        {"name": "Charlie", "age": 40},
    ]
    expected = [
        {"name": "Anna", "age": 30},
        {"name": "Ivan", "age": 25},
        {"name": "Charlie", "age": 40},
    ]
    assert filter_by_age(users, 25) == expected


def test_filter_by_age_empty():
    assert filter_by_age([], 25) == []


def test_filter_by_age_all_below():
    users = [
        {"name": "Anna", "age": 20},
        {"name": "Bob", "age": 15},
        {"name": "Ivan", "age": 10},
    ]
    assert filter_by_age(users, 25) == []


def test_filter_by_age_missing_age():
    users = [
        {"name": "Anna", "age": 30},
        {"name": "Bob"},
        {"name": "Ivan", "age": 25},
    ]
    expected = [
        {"name": "Anna", "age": 30},
        {"name": "Ivan", "age": 25},
    ]
    assert filter_by_age(users, 25) == expected


def test_count_by_status():
    items = [
        {"id": 1, "status": "active"},
        {"id": 2, "status": "inactive"},
        {"id": 3, "status": "active"},
        {"id": 4},
    ]
    expected = {"active": 2, "inactive": 1}
    assert count_by_status(items) == expected


def test_count_by_status_empty():
    assert count_by_status([]) == {}


def test_count_by_status_all_missing():
    items = [{"id": 1}, {"id": 2}, {"id": 3}]
    assert count_by_status(items) == {}


def test_count_by_status_all_same():
    items = [
        {"id": 1, "status": "active"},
        {"id": 2, "status": "active"},
        {"id": 3, "status": "active"},
    ]
    expected = {"active": 3}
    assert count_by_status(items) == expected


def test_count_by_status_mixed():
    items = [
        {"id": 1, "status": "active"},
        {"id": 2, "status": "inactive"},
        {"id": 3, "status": "active"},
        {"id": 4, "status": "pending"},
        {"id": 5},
    ]
    expected = {"active": 2, "inactive": 1, "pending": 1}
    assert count_by_status(items) == expected
