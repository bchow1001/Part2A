def heapify(arr, n, i):
    """
    Maintains the max-heap property.
    n: size of the heap
    i: index of the current root node
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a maxheap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap root with end
        heapify(arr, i, 0) # Heapify the reduced heap

# Example Usage
data = [12, 11, 13, 5, 6, 7]
heap_sort(data)
print("Sorted array (Heap Sort):", data)
