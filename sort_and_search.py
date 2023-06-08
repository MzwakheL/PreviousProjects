def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
x = 9

# Perform linear search
result = linear_search(arr, x)

if result == -1:
    print("Element not found in array")
else:
    print(f"Element found at index {result}")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Sort the array using insertion sort
insertion_sort(arr)

print(arr)

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Sort the array using insertion sort
insertion_sort(arr)

x = 9

# Perform binary search
result = binary_search(arr, x)

if result == -1:
    print("Element not found in array")
else:
    print(f"Element found at index {result}")
