'''
1. Research about the `Bubble Sort Algorithm` in Python. Implement three version of it:
- In ascending order (regular one)
- In descending order
- With early stopping
'''
from typing import List


# In ascending order (regular one)
def bubble_sort_ascending_order(list_to_sort: List[int]) -> List[int]:
    for i in range(len(list_to_sort)):
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[j], list_to_sort[i] = list_to_sort[i], list_to_sort[j]
    return list_to_sort


# In descending order
def bubble_sort_descending_order(list_to_sort: List[int]) -> List[int]:
    for i in range(len(list_to_sort)):
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i] < list_to_sort[j]:
                list_to_sort[j], list_to_sort[i] = list_to_sort[i], list_to_sort[j]
    return list_to_sort


# With early stopping
def bubble_sort_with_early_stopping(list_to_sort: List[int]) -> List[int]:
    for i in range(len(list_to_sort)):
        swapped = False
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[j], list_to_sort[i] = list_to_sort[i], list_to_sort[j]
                swapped = True
        if not swapped:  # if no changes were made during the inner loop, then the list is already sorted
            break

    return list_to_sort


ACCEPTED_ORDERS = {'asc', 'desc'}


def bubble_sort_with_option_to_sort(list_to_sort: List[int], order: str = 'asc') -> List[int] | str:
    if order not in ACCEPTED_ORDERS:
        return "The order option is invalid. Accepted values are: 'asc' for Ascending Order or 'desc' for Descending Order"

    for i in range(len(list_to_sort)):
        swapped = False
        for j in range(i + 1, len(list_to_sort)):
            if order == 'asc':
                if list_to_sort[i] > list_to_sort[j]:
                    list_to_sort[j], list_to_sort[i] = list_to_sort[i], list_to_sort[j]
                    swapped = True
            elif order == 'desc':
                if list_to_sort[i] < list_to_sort[j]:
                    list_to_sort[j], list_to_sort[i] = list_to_sort[i], list_to_sort[j]
                    swapped = True

        if not swapped:  # if no changes were made during the inner loop, then the list is already sorted
            break

    return list_to_sort


list_to_test = [2, 5, 1, 3, 7, 1, 6, 2, 5]
print(f"Using ascending order: {bubble_sort_ascending_order(list_to_test)}")
print(f"Using descending order: {bubble_sort_descending_order(list_to_test)}")
print(f"Using early stop strategy: {bubble_sort_with_early_stopping(list_to_test)}")
print(f"Using with chosen option in ascending order: {bubble_sort_with_option_to_sort(list_to_test, 'asc')}")
print(f"Using with chosen option in descending order: {bubble_sort_with_option_to_sort(list_to_test, 'desc')}")
print(f"Using with chosen an invalid option: {bubble_sort_with_option_to_sort(list_to_test, 'inv')}")

"""
Output:
    Using ascending order: [1, 1, 2, 2, 3, 5, 5, 6, 7]
    Using descending order: [7, 6, 5, 5, 3, 2, 2, 1, 1]
    Using early stop strategy: [1, 1, 2, 2, 3, 5, 5, 6, 7]
    Using with chosen option in ascending order: [1, 1, 2, 2, 3, 5, 5, 6, 7]
    Using with chosen option in descending order: [7, 6, 5, 5, 3, 2, 2, 1, 1]
    Using with chosen an invalid option: The order option is invalid. Accepted values are: 'asc' for Ascending Order or 'desc' for Descending Order
"""