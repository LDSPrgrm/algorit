import random
import string
import time

def get_time_complexity(searching_algorithm, list, keyword):
    start = time.perf_counter()
    searching_algorithm(list, keyword)
    print("All done at %.20f seconds." % (time.perf_counter() - start))

def generate_random_strings(num_strings):
    random_strings = []
    for i in range(num_strings):
        length = random.randint(5, 15)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        random_strings.append(random_string)
    return random_strings

def linear_search(list, keyword):
    matches = 0
    for word in list:
        if word.casefold() == keyword:
            print(f"Found {word} in the array.")
            matches += 1
    print(f"Found {matches} result/s.")
  
def binary_search(list, keyword):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        current_word = list[mid].casefold()
        if current_word == keyword:
            print(f"Found {list[mid]} at index {mid}")
            return
        elif current_word > keyword:
            high = mid - 1
        else:
            low = mid + 1
    print(f"{keyword} not found in the array.")
    
string_list = generate_random_strings(100)
def main():
    string_list.sort()
    print(string_list)
    while True:
        keyword = input("Search a keyword (or 'exit' to quit): ")
        if (keyword == "exit"):
            break
        
        print("Linear Search Results:")
        get_time_complexity(linear_search, string_list, keyword.casefold())
        print()
        print("Sorting started.")
        print("Sorting finished.\n")
        print("Binary Search Results:")
        get_time_complexity(binary_search, string_list, keyword.casefold())

if __name__ == "__main__":
    main()