import random
import time

class Algorithms:
    def __init__(self, lower_bound, upper_bound, array_size, manual_array, target_element=None, input_type=None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.array_size = array_size
        self.target_element = target_element
        self.input_type = input_type
        self.manual_array = manual_array

        
    def generate_array(self):
        # Generate a random array based on the given size and bounds
        return [random.randint(self.lower_bound, self.upper_bound) for _ in range(self.array_size)]
    
    def random_choice(self):
        self.random_array = self.generate_array()

    # Placeholder for Bubble Sort
    def bubble_sort(self):
        pass  # Implement Bubble Sort here

    # Placeholder for Merge Sort
    def merge_sort(self):
        pass  # Implement Merge Sort here

    # Placeholder for Quick Sort
    def quick_sort(self):
        pass  # Implement Quick Sort here

    # Placeholder for Radix Sort
    def radix_sort(self):
        pass  # Implement Radix Sort here

    # Placeholder for Linear Search
    def linear_search(self):
        # Implement Linear Search to find self.target_element in self.array
        pass  # You can search the array for self.target_element

# Example usage:
if __name__ == "__main__":
    print()
    # FOR TESTING PUPOSES

    # # Example parameters
    # lower_bound = 1
    # upper_bound = 100
    # array_size = 10
    # target_element = 50
    
    # sorting = Algorithms(lower_bound, upper_bound, array_size, target_element)
    
    # # Example method calls (you can implement them later)
    # sorting.bubble_sort()
    # sorting.merge_sort()
    # sorting.quick_sort()
    # sorting.radix_sort()
    # sorting.linear_search()
    
    # print("Generated Array:", sorting.array)  # You can see the generated array here