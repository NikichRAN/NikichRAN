"""
get_index it`s function recursive binary search.
You can use it for search index element in array.
You can use it for sorted array, only!
And it has length limit of the input array,
it`s 2**1000 elements.
This script consist 2 functions.
binary_search is supporting function.
You can use function get_index for search index element in array!
"""
from typing import Optional, Union, List


def get_index(array: List[Union[float, int]], element: Union[float, int]) -> Optional[int]:
    """
    This function return element index. It search range for the first binary_search call.
    And call binary_search function.
    :param array: input array(Python list), it`s consist with float or integer numbers
    :param element: float or integer number whose index needs to be search
    :return: if element is located in array get_index return element index,
    if element isn`t located in array get_index return None
    """
    len_arr = len(array)
    if len_arr > 2**1000:
        raise ValueError('The incoming array must not exceed 2**1000 elements')
    first = array[0]
    penultimate = array[len_arr - 1]
    index = binary_search(array, element, first, penultimate)
    return index


def binary_search(array, element, left_boundary, right_boundary):
    """
    The binary_search function performs a recursive search for the index of an element in an array.
    For the first function call, we must pass left_boundary and right_boundary
    :param array: at the same as get_index
    :param element: at the same as get_index
    :param left_boundary: the beginning of the search range on the first call of the function
    :param right_boundary: the end of the search range on the first call of the function
    :return: at the same as get_index
    """
    if left_boundary > right_boundary:  # if right boundary exceed left boundary
        return None  # hence the element don`t located in array

    middle = (right_boundary + left_boundary) // 2  # search the middle of an array
    if array[middle] == element:  # if element is located in the middle of array
        return middle  # hence return this index
    elif element < array[middle]:  # if necessary element smaller than the element in the middle array
        # hence we use recursive binary search in left half
        return binary_search(array, element, left_boundary, middle - 1)
    else:  # in other case in right half
        return binary_search(array, element, middle + 1, right_boundary)


#element = int(input('gg'))
element = 55550000000000
array = [i for i in range(1, 100000000000000)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
#print(binary_search(array, element, 0, 98))

print(get_index(array, element))