import time
import random

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
def test_heap_sort():
    # Test Cases
    test_cases = {
        "Random List": [random.randint(0, 100) for _ in range(10)],
        "Already Sorted": [1, 2, 3, 4, 5],
        "Reverse Sorted": [5, 4, 3, 2, 1],
        "Empty List": [],
        "Single Element": [42]
    }

    print("--- Heap Sort Functional Testing ---")
    for name, data in test_cases.items():
        original = data.copy()
        heap_sort(data)
        success = (data == sorted(original))
        print(f"{name:15}: {'PASSED' if success else 'FAILED'} | Result: {data}")

# Run Test
test_heap_sort()
print("Try programiz.pro")