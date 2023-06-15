from typing import List


def bubble_sort(arr: List[str]) -> List[str]:
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print(f"Pass {i + 1}: {arr}")

    return arr


# def insertion_sort(arr: List[tuple]) -> List[str]:
#     n = len(arr)
#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and (
#             arr[j][0] > key[0] or (arr[j][0] == key[0] and arr[j][1] > key[1])
#         ):
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key

#         print(f"Pass {i}: {[admin_no for _, admin_no in arr]}")

#     return [admin_no for _, admin_no in arr]


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
