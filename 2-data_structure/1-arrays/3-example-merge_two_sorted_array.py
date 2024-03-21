# merged to sorted array :
from typing import List


# O(n) but pad space complexity and readability
def merge_two_sort_array(arr1: List[int], arr2: List[int]):

    res = []
    larger_len = len(arr1) if len(arr1) > len(arr2) else len(arr2)
    arr1_current_index = 0
    arr2_current_index = 0

    while arr1_current_index < larger_len or arr2_current_index < larger_len:

        if arr1_current_index == len(arr1) or arr2_current_index == len(arr2):
            if arr2_current_index < len(arr2):
                res += arr2[arr2_current_index:]
            elif arr1_current_index < len(arr1):
                res += arr1[arr1_current_index:]
            break

        if arr1[arr1_current_index] <= arr2[arr2_current_index]:
            res.append(arr1[arr1_current_index])
            arr1_current_index += 1
            continue

        if arr2[arr2_current_index] <= arr1[arr1_current_index]:
            res.append(arr2[arr2_current_index])
            arr2_current_index += 1
            continue

    return res


# O(n)
def merge_two_sorted_arrays2(arr1: List[int], arr2: List[int]) -> List[int]:
    # Initialize pointers for arr1 and arr2
    i, j = 0, 0
    # Initialize the result array
    result = []

    # Traverse both arrays and append smaller of both elements in result
    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
            print(f" i : {i}, j : {j}")
        else:
            result.append(arr2[j])
            j += 1
            print(f" i : {i}, j : {j}")

    # Store remaining elements of first array
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Store remaining elements of second array
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


# O(n^2)
def merge_two_sort_array3(arr1: List[int], arr2: List[int]):

    res = []
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while arr1 or arr2:
        if not arr1 or not arr2:
            if arr1:
                res += arr1
            if arr2:
                res += arr2
            break

        if arr1[0] < arr2[0]:
            res.append(arr1[0])
            del arr1[0]  # this operation will be O(n)
        else:
            res.append(arr2[0])
            del arr2[0]
    return res
