import time
import random

def generate_random_list():
    return [random.randint(1, 100) for _ in range(100)]

def get_time_complexity(sorting_algorithm, unsorted_list):
    start = time.perf_counter()
    sorting_algorithm(unsorted_list)
    print("All done at %.20f seconds." % (time.perf_counter() - start))

def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(n-i-1):
            if(unsorted_list[j] > unsorted_list[j+1]):
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    
def selection_sort(unsorted_list):
    n = len(unsorted_list)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if(unsorted_list[min_index] > unsorted_list[j]):
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

def insertion_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1
        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        unsorted_list[j + 1] = key
    

def main():
    unsorted_list = generate_random_list()
    bubble_list = unsorted_list[:]
    selection_list = unsorted_list[:]
    insertion_list = unsorted_list[:] 
    
    print("Unsorted: \n", unsorted_list)
    print()
    
    print("Bubble Sort")
    get_time_complexity(bubble_sort, bubble_list)
    print("Sorted: \n", bubble_list)
    print()
    
    print("Selection Sort")
    get_time_complexity(selection_sort, selection_list)
    print("Sorted: \n", selection_list)
    print()
    
    print("Insertion Sort")
    get_time_complexity(insertion_sort, insertion_list)
    print("Sorted: \n", insertion_list)
    print()
    
main()