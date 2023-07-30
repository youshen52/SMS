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


def selection_sort(arr: List[tuple]) -> List[str]:
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])
        print(f"Pass {i}: {[admin_no for _, admin_no in arr]}")

    return [admin_no for _, admin_no in arr]


def merge_sort(arr: List[tuple]) -> List[tuple]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)


def _merge(left: List[tuple], right: List[tuple]) -> List[tuple]:
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][0] < right[right_index][0]:
            merged.append(left[left_index])
            left_index += 1
        elif left[left_index][0] > right[right_index][0]:
            merged.append(right[right_index])
            right_index += 1
        else:
            if left[left_index][1] <= right[right_index][1]:
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


# Sample student data (replace this with your actual student data)
students_data = [
    {"id": 1, "admin": "123456D", "name": "Jon", "age": 18},
    {"id": 2, "admin": "232345D", "name": "John", "age": 19},
    {"id": 3, "admin": "123456A", "name": "Ocean", "age": 20},
    {"id": 4, "admin": "123456A", "name": "hello", "age": 21},
]


def print_students_recursive(students, n, current_row=0):
    if not students:
        return

    students_in_row = students[:n]
    for student in students_in_row:
        print(f"id: {student['id']}", end="             ")
    print()

    for student in students_in_row:
        print(f"admin: {student['admin']}", end="    ")
    print()

    for student in students_in_row:
        print(f"name: {student['name']}", end="         ")
    print()

    for student in students_in_row:
        print(f"age: {student['age']}", end="           ")

    print()
    print()

    print_students_recursive(students[n:], n, current_row + 1)


