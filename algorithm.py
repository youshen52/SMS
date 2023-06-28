from typing import List


def bubble_sort(arr: List[str]) -> List[str]:
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print(f"Pass {i + 1}: {arr}")

    return arr


def insertion_sort(arr: List[tuple]) -> List[str]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"Pass {i}: {[admin_no for _, admin_no in arr]}")

    return [admin_no for _, admin_no in arr]


def selection_sort(arr: list[str]) -> List[str]:
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])


from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged
