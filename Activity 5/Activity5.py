import time
import random

def generate_random_list():
    return [random.randint(1, 100) for _ in range(100000)]

def get_time_complexity(sorting_algorithm, unsorted_list):
    start = time.perf_counter()
    sorting_algorithm(unsorted_list)
    print("All done at %.20f seconds." % (time.perf_counter() - start))

def merge_sort(unsorted_list):
    n = len(unsorted_list)
    if (n > 1):
        mid = n // 2
        left_half = unsorted_list[:mid]
        right_half = unsorted_list[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        merge(unsorted_list, left_half, right_half)
        
def merge(unsorted_list, left_half, right_half):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            unsorted_list[k] = left_half[i]
            i += 1
        else:
            unsorted_list[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        unsorted_list[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        unsorted_list[k] = right_half[j]
        j += 1
        k += 1
        
def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, low, high):
    if low < high:
        pivot_index = _partition(arr, low, high)

        _quicksort(arr, low, pivot_index - 1)
        _quicksort(arr, pivot_index + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    unsorted_list = generate_random_list()
    merge_list = unsorted_list[:]
    quick_list = unsorted_list[:] 
    
    print("Unsorted: \n", unsorted_list)
    print()
    
    print("Merge Sort")
    get_time_complexity(merge_sort, merge_list)
    print("Sorted: \n", merge_list)
    print()
    
    print("Quicksort")
    get_time_complexity(quicksort, quick_list)
    print("Sorted: \n", quick_list)
    print()
    
main()