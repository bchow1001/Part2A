import time

def heap_sort(arr):
    """
    Implements Heap Sort - O(n log n) complexity.
    This demonstrates linearithmic growth by using a Max-Heap structure.
    """
    def heapify(n, i):
        largest, l, r = i, 2*i + 1, 2*i + 2
        if l < n and arr[l] > arr[largest]: largest = l
        if r < n and arr[r] > arr[largest]: largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(i, 0)

def towers_of_hanoi(n, src, dest, aux):
    """
    Implements Towers of Hanoi - O(2^n) complexity.
    This demonstrates exponential growth through recursive doubling.
    """
    if n > 0:
        towers_of_hanoi(n - 1, src, aux, dest)
        # print(f"Move disk {n} from {src} to {dest}") # Commented out for large N tests
        towers_of_hanoi(n - 1, aux, dest, src)

# Main execution block to demonstrate the code works
if __name__ == "__main__":
    test_list = [19, 2, 31, 45, 6, 11]
    print("Original List:", test_list)
    heap_sort(test_list)
    print("Sorted List (Heap Sort):", test_list)
    
    print("\nRunning Towers of Hanoi (3 disks)...")
    towers_of_hanoi(3, 'A', 'C', 'B')
    print("Hanoi completed successfully.")