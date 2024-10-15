from __future__ import annotations

from typing import Callable, List, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def partition(my_list: List[T], low: int, high: int, sort_key: Callable[[T], K] = lambda x: x) -> int:
    """
    Partitions the list based on a chosen pivot

    Args:
        my_list (List[T]): The list to sort
        low (int): The lower bound of the list
        high (int): The upper bound of the list
        sort_key (Callable[[K], bool]): The function to sort the list

    Returns:
        The new index of the pivot

    Complexity:
        Best/Worst Case: O(N * comp(K)) where N is the length of the list, K is the size of the sort_key
    """
    pivot: T = my_list[high]
    i: int = low - 1

    for j in range(low, high):
        if sort_key(my_list[j]) < sort_key(pivot):
            i += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]

    my_list[i + 1], my_list[high] = my_list[high], my_list[i + 1]
    return i + 1


def quicksort_aux(my_list: List[T], low: int, high: int, sort_key: Callable[[T], K] = lambda x: x) -> None:
    """
    Args:
        my_list (List[T]): The list to sort
        low (int): The lower bound of the list
        high (int): The upper bound of the list
        sort_key (Callable[[K], bool]): The function to sort the list

    Returns:
        The sorted list

    Complexity:
        Best Case: O(NlogN * comp(K))
        Worst Case: O(N^2 * comp(K)) where N is the length of the list, K is the size of the sort_key
    """
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(my_list, low, high, sort_key)

        quicksort_aux(my_list, low, pi - 1, sort_key)
        quicksort_aux(my_list, pi + 1, high, sort_key)


def quicksort(my_list: List[T], sort_key: Callable[[T], K] = lambda x: x) -> None:
    """
    Sort a list using the quicksort operation.

    Args:
        my_list (List[T]): The list to sort
        sort_key (Callable[[K], bool]): The function to sort the list

    Returns:
        The sorted list

    Complexity:
        Best Case: O(NlogN * comp(K))
        Worst Case: O(N^2 * comp(K)) where N is the length of the list, K is the size of the sort_key
    """
    return quicksort_aux(my_list, 0, len(my_list) - 1, sort_key)
