from __future__ import annotations

from typing import Callable, List, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def merge(list1: List[T], list2: List[T], sort_key: Callable[[T], K] = lambda x: x) -> List[T]:
    """
    Merges two sorted lists into one larger sorted list,
    containing all elements from the smaller lists.

    The `key` kwarg allows you to define a custom sorting order.

    Args:
        list1 (List[T]): First sub-list
        list2 (List[T]): Second sub-list
        sort_key (Callable[[K], bool]): The function to sort the list

    Returns:
        The sorted list

    Pre-Condition:
        Both l1 and l2 are sorted, and contain comparable elements.

    Complexity:
        Best/Worst Case O(n * comp(K)), n = len(l1)+len(l2), K is the size of the sort_key
    """
    new_list: List = []
    cur_left: int = 0
    cur_right: int = 0

    while cur_left < len(list1) and cur_right < len(list2):
        if sort_key(list1[cur_left]) <= sort_key(list2[cur_right]):
            new_list.append(list1[cur_left])
            cur_left += 1
        else:
            new_list.append(list2[cur_right])
            cur_right += 1

    new_list += list1[cur_left:]
    new_list += list2[cur_right:]
    return new_list


def mergesort(my_list: List[T], sort_key: Callable[[T], K] = lambda x: x) -> List[T]:
    """
    Sort a list using the mergesort operation.

    Args:
        my_list (List[T]): The list to sort
        sort_key (Callable[[K], bool]): allows you to define a custom sorting order

    Returns:
        The sorted list

    Complexity:
        Best/Worst Case O(NlogN * comp(K)) where N is the length of the list, K is the size of the sort_key
    """
    if len(my_list) <= 1:
        return my_list

    break_index: int = (len(my_list)+1) // 2
    l1 = mergesort(my_list[:break_index], sort_key)
    l2 = mergesort(my_list[break_index:], sort_key)
    return merge(l1, l2, sort_key)
