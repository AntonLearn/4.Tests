import pytest
from main_task_1 import max_in_list, len_of_list, find_ind_elem_in_list


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([-5, 0, 10, 5], 10),
        ([3, 7, -6, 9, 15, 0, -1], 15)
    ]
)
def test_max_in_list(lst, expected):
    assert max_in_list(lst) == expected


@pytest.mark.parametrize(
    'lst, expected',
    [
        ([-5, 0, 10, 5], 4),
        ([3, 7, -6, 9, 15, 0, -1], 7),
        (['a', 'b'], 2)
    ]
)
def test_len_of_list(lst, expected):
    assert len_of_list(lst) == expected


@pytest.mark.parametrize(
    'lst, el, expected',
    [
        ([-5, 0, 10, 5], 10, 2),
        ([3, 7, -6, 9, 15, 0, -1], 7, 1),
        (['a', 'b'], 'a', 0)
    ]
)
def test_find_ind_elem_in_list(lst, el, expected):
    assert find_ind_elem_in_list(lst, el) == expected