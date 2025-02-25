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
        self.timeTaken = [0] * 5
        self.random_array = []

        
    def generate_array(self):
        # Generate a random array based on the given size and bounds
        random_array = [random.randint(self.lower_bound, self.upper_bound) for _ in range(self.array_size)]
        return random_array
    
    
    def random_choice(self):
        self.random_array = self.generate_array()


    """
    BUBBLE SORT
    """
    def bubble_sort(self):
        if self.input_type == "Random":
            if not self.random_array:  
                self.random_choice()
            myArray = self.random_array[:]  
        else:
            myArray = self.manual_array[:]

        n = len(myArray)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if myArray[j] > myArray[j + 1]:  
                    myArray[j], myArray[j + 1] = myArray[j + 1], myArray[j]
                    swapped = True
            if not swapped: 
                break
       # print(f"This is my array after sorting: {myArray}")



    """
    MERGE SORT
    """

    
    def merge_sort(self):
        
        if self.input_type == "Random":
            if not self.random_array:
                self.random_choice()
            array = self.random_array
        else:
            array = self.manual_array

        def merge_sort_recursive(arr):
            
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort_recursive(left_half)
                merge_sort_recursive(right_half)

                # Mergin' da halves
                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                # Add em, lads
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort_recursive(array)  # Calling the inner function (so it works)





    """
    QUICK SORT
    """

    def quick_sort(self):
        # Choose which array to sort based on input type
        if self.input_type == "Random":
            if not self.random_array:
                self.random_choice()
            array = self.random_array
        else:
            array = self.manual_array

        # Call the recursive quick_sort function and store the sorted result back
        sorted_array = self.quick_sort_recursive(array)
        return sorted_array

    def quick_sort_recursive(self, arr):
        # Base case: array of length 1 or less is already sorted
        if len(arr) <= 1:
            return arr

        # Choose the pivot (we use the middle element in this case)
        pivot = arr[len(arr) // 2]

        # Partition the array into three parts: left, middle, and right
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively sort the left and right parts, and combine them with the middle
        return self.quick_sort_recursive(left) + middle + self.quick_sort_recursive(right)
    
        
    """
    RADIX SORT
    """

    def radix_sort(self):
        """Performs Radix Sort on self.random_array or self.manual_array (only for integers)."""
        if self.input_type == "Random":
            if not self.random_array:
                self.random_choice()
            array = self.random_array
        else:
            array = self.manual_array

        if not array:
            return

        def counting_sort(arr, exp):
            """A stable Counting Sort used in Radix Sort based on digit at exponent exp."""
            n = len(arr)
            output = [0] * n
            count = [0] * 10  # Because digits range from 0-9

            # Count occurrences of each digit in the current place value
            for num in arr:
                index = (num // exp) % 10
                count[index] += 1

            # Compute cumulative count
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Build the output array (placing numbers in correct order)
            for i in range(n - 1, -1, -1):  # Process from right to left for stability
                num = arr[i]
                index = (num // exp) % 10
                output[count[index] - 1] = num
                count[index] -= 1

            # Copy the sorted numbers back into arr
            for i in range(n):
                arr[i] = output[i]

        # Get the maximum number to determine the number of passes
        max_num = max(array)

        # Perform Counting Sort for each digit place (1s, 10s, 100s, etc.)
        exp = 1
        while max_num // exp > 0:
            counting_sort(array, exp)
            exp *= 10




    # Placeholder for Linear Search
    def linear_search(self):
        if self.input_type == "Random":
            if not self.random_array:  
                self.random_choice()
            myArray = self.random_array[:]  
        else:
            myArray = self.manual_array[:]
        for index in range(len(myArray)):
            if myArray[index] == self.target_element:
                return index
        return -1
    


    def run(self):
        start_time = 0
        end_time = 0
        while(self.timeTaken[0] == 0.0):
            start_time = time.time()
            self.bubble_sort()
            end_time = time.time()
            # Bubble Sort
            self.timeTaken[0] = (end_time - start_time) * 1000
        
        print(f"Bubble Sort Time: {(end_time - start_time) * 1000:.30f}")
        print(f"Time taken array {self.timeTaken}")
        # Merge Sort
        while(self.timeTaken[1] == 0.0):
            start_time = time.time()
            self.merge_sort()
            end_time = time.time()
            # Merge Sort
            self.timeTaken[1] = (end_time - start_time) * 1000
        
        print(f"Merge Sort Time: {(end_time - start_time) * 1000:.30f}")
        print(f"Time taken array {self.timeTaken}")

        # Quick Sort
        while(self.timeTaken[2] == 0.0):
            start_time = time.time()
            self.quick_sort()
            end_time = time.time()
            # Quick Sort
            self.timeTaken[2] = (end_time - start_time) * 1000
        
        print(f"Quick Sort Time: {(end_time - start_time) * 1000:.30f}")
        print(f"Time taken array {self.timeTaken}")
        
        # Radix Sort
        while(self.timeTaken[3] == 0.0):
            start_time = time.time()
            self.radix_sort()
            end_time = time.time()
            # Radix Sort
            self.timeTaken[3] = (end_time - start_time) * 1000
        
        print(f"Radix Sort Time: {(end_time - start_time) * 1000:.30f}")
        print(f"Time taken array {self.timeTaken}")

        # Linear Search
        while(self.timeTaken[4] == 0.0):
            start_time = time.time()
            self.linear_search()
            end_time = time.time()
            # Linear Sort
            self.timeTaken[4] = (end_time - start_time) * 1000
        
        print(f"Linear Sort Time: {(end_time - start_time) * 1000:.30f}")
        print(f"Time taken array {self.timeTaken}")


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