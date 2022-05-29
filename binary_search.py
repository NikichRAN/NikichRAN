"""
This is function binary search.
You can use it for search index element in array.
You can use it for sorted array, only!
binary_search function use loop to divide the range in half.
With each cycle pass, the range decreases by a factor of 2.
"""


from typing import Optional, Union, List


def binary_search(array: List[Union[float, int]],
                  element: Union[float, int]) -> Optional[int]:
    """
    :param array: input array(Python list), it`s consist with float or integer numbers
    :param element: float or integer number whose index needs to be search
    :return: if element is located in array get_index return element index,
    if element isn`t located in array get_index return None
    """
    if sorted(array) != array:  # in put array must be sorted, else exception!
        raise ValueError('In put array must be sorted')
    low = 0  # The beginning of the search range
    high = len(array) - 1  # The end of the search range
    while low <= high:
        mid = (high + low)//2  # It`s middle of the range
        guess = array[mid]  # Array element in the middle
        if guess == element:
            return mid
        if guess > element:  # Continue search in right part
            high = mid - 1
        else:
            low = mid + 1  # Continue search in left part
    return None  # If the element don`t located in array
