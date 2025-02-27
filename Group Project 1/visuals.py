import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import random

class SortingVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
   

        # Modern stylesheet for better looking UI
        self.setStyleSheet("""
            QPushButton {
                background-color: #0078D7;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid gray;
                border-radius: 5px;
            }
            QMainWindow {
                background-color: #2E3440;
            }
        """)


        # Error checking for passing data through the files
        if len(sys.argv) != 6:
            print("Usage: visuals.py <arraySize> <lowerBound> <upperBound>")
            return

        try:
            # Read values given from main.py in the form of command-line arguments
            self.arraySize = int(sys.argv[1])
            self.lowerBound = int(sys.argv[2])
            self.upperBound = int(sys.argv[3])
            self.manualArray = list(map(int, sys.argv[4].split(',')))
            self.permManualArray = list(map(int, sys.argv[4].split(',')))
            
            self.targetElement =  int(sys.argv[5])
            print(f"Received values: arraySize={self.arraySize}, lowerBound={self.lowerBound}, upperBound={self.upperBound}, manualArray={self.manualArray}, targetElement={self.targetElement}")
            print(f"2 This is manual array {self.manualArray}")
           

        except ValueError:
            print("Invalid input. Please ensure all inputs are integers.")


        


        # Menu-ing buttons, drop down menus, name of visualizer
        self.setWindowTitle("Sorting Algorithm Visualizer")
        self.setGeometry(100, 100, 800, 600)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        self.algoSelector = QComboBox(self)
        self.algoSelector.addItems(["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search"])
        layout.addWidget(self.algoSelector)

        self.startButton = QPushButton("Start Sorting", self)
        self.startButton.clicked.connect(self.runSorting)
        layout.addWidget(self.startButton)

        self.pauseButton = QPushButton("Pause", self)
        self.pauseButton.clicked.connect(self.togglePause)
        layout.addWidget(self.pauseButton)

        self.endButton = QPushButton("End Sorting", self)
        self.endButton.clicked.connect(self.endSorting)
        layout.addWidget(self.endButton)
        
        self.resetButton = QPushButton("Reset", self)
        self.resetButton.clicked.connect(self.resetSorting)
        layout.addWidget(self.resetButton)

        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.isPaused = False
        self.isStopped = False

        self.numElements = self.arraySize
        if (self.arraySize == 0):
            self.array = self.manualArray
            self.numElements = len(self.manualArray)
        else:
            self.array = [random.randint(self.lowerBound, self.upperBound) for _ in range(self.numElements)]
            self.targetElement = np.random.choice(self.array)

        print(f"This is the array {self.array} of type: {type(self.array)}")
        self.drawBars()






    # Function that draws the visualizer, decides it's colors, axis, updates UI whenever called
    def drawBars(self, colors=None):
        self.ax.clear()
        
        self.ax.set_facecolor("#2E3440")
        if colors is None:
            colors = ["#4E7F7A"] * self.numElements # Color of the bars, in this case, teal green
        self.ax.bar(range(len(self.array)), self.array, color=colors)
        self.ax.set_title("Sorting Visualization")
        
        self.ax.tick_params(axis="x", colors="black")
        self.ax.tick_params(axis="y", colors="black")

        self.canvas.draw()

    # Function used to connect the visualizer to the sorting functions once input is chosen
    def runSorting(self):
        self.isStopped = False
        selectedAlgo = self.algoSelector.currentText()

        if selectedAlgo == "Bubble Sort":
            self.bubbleSort()
        elif selectedAlgo == "Merge Sort":
            self.mergeSort(0, len(self.array) - 1)
        elif selectedAlgo == "Quick Sort":
            self.quickSort(0, len(self.array) - 1)
        elif selectedAlgo == "Radix Sort":
            self.radixSort()
        elif selectedAlgo == "Linear Search":
            self.linearSearch()

    # Pauses, changes Pause button to Resume if Pause is pressed
    def togglePause(self):
        self.isPaused = not self.isPaused
        self.pauseButton.setText("Resume" if self.isPaused else "Pause")

    # Stops all sorting, resets the pause button, UI will be updated
    def endSorting(self):
      
        self.isStopped = True
        self.isPaused = False
        self.pauseButton.setText("Pause")
        self.drawBars()
        

    # Resets the sorting visualizer to its original state so all sorting algos can be tested
    def resetSorting(self):
        self.isStopped = True
        self.isPaused = False
        self.pauseButton.setText("Pause")

        if self.arraySize == 0:  
            self.array = self.permManualArray.copy() 
        else:  
            self.array = [random.randint(self.lowerBound, self.upperBound) for _ in range(self.numElements)]
            self.targetElement = np.random.choice(self.array)
        self.drawBars()

    # Pauses the sorting until it resumes or stops
    def waitForResume(self):
        while self.isPaused:
            QApplication.processEvents()
            time.sleep(0.1)
            if self.isStopped:
                return False
        return True


    """
    BUBBLE SORT
    """

    # The visualizer for bubble sort, includes options to pause/stop during the process
    def bubbleSort(self):
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - 1 - i):
                if self.isStopped:
                    return

                self.drawBars(["red" if x == j or x == j + 1 else "blue" for x in range(self.numElements)])

                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.drawBars(["red" if x == j or x == j + 1 else "blue" for x in range(self.numElements)])
                    QApplication.processEvents()
                    time.sleep(0.1)

                # Should we pause and stop?
                if not self.waitForResume():
                    return

        self.drawBars(["green"] * self.numElements)





    """
    MERGE SORT
    """

    def mergeSort(self, left, right):
        if left < right:
            if self.isStopped:
                return
            
            mid = (left + right) // 2
            
            # Use recursion to sort both left and right halves
            self.mergeSort(left, mid)
            self.mergeSort(mid + 1, right)
            
            
            self.visualizeMerge(left, mid, right)
            
            # Should we pause and stop?
            if not self.waitForResume():
                return
            
    # A visualizer for Merge during the merging step, which doesn't change the actual array
    def visualizeMerge(self, left, mid, right):
     
        if self.isStopped:
            return
        
        # Temp arrays for both halves
        left_half = self.array[left:mid+1]
        right_half = self.array[mid+1:right+1]
        
        # Temporary merged array (this is what we visualize)
        merged = []
        i, j = 0, 0
        
        # Merge the two halves (without changing the original array)
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1
        
        # If there are remaining elements in the left half, append them
        while i < len(left_half):
            merged.append(left_half[i])
            i += 1
        
        # If there are remaining elements in the right half, append them
        while j < len(right_half):
            merged.append(right_half[j])
            j += 1
        
        # Visualize the complete merged array of both halves
        merged_index = 0
        for k in range(left, right + 1):
            # Coloring the elements as yellow once completed to help differentiate
            if merged_index < len(merged):
                self.array[k] = merged[merged_index]
                merged_index += 1

        # Update the visualization with the current state of the array
        self.drawBars(["yellow" if left <= x <= right else "blue" for x in range(self.numElements)])
        
        QApplication.processEvents()
        time.sleep(0.1)
        
        # Should we pause and stop?
        if not self.waitForResume():
            return
        
        # Visualize the final sorted portion as green
        self.drawBars(["green" if left <= x <= right else "blue" for x in range(self.numElements)])
        QApplication.processEvents()
        time.sleep(0.1)


    """
    QUICK SORT
    """

    def quickSort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            if pivot is None:
                print(f"Error: partition returned None. low={low}, high={high}")
                return  # Avoid recursion if partition fails & recursively sort the two halves
            self.quickSort(low, pivot - 1)
            self.quickSort(pivot + 1, high)
        self.drawBars(["green"] * self.numElements)


    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.isStopped:
                return

                # Visualize the comparison: red for the current element and pivot
            self.drawBars(["red" if x == j else "orange" if x == high else "blue" for x in range(self.numElements)])

            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

                    # Highlight swapped elements in yellow
                self.drawBars(["yellow" if x == i or x == j else "blue" for x in range(self.numElements)])
                QApplication.processEvents()
                time.sleep(0.1)

            if not self.waitForResume():
                return

            # Swap the pivot into the correct position
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]

            # Highlight the pivot placement in green
        self.drawBars(["green" if x == i + 1 else "blue" for x in range(self.numElements)])
        QApplication.processEvents()
        time.sleep(0.1)

        return i + 1  # Return the pivot index




    """
    RADIX SORT
    """
    # def radixSort(self):
    #     max_val = max(self.array)
    #     exp = 1
    #     while max_val // exp > 0:
    #         self.countingSort(exp)
    #         exp *= 10

    # def countingSort(self, exp):
    #     output = [0] * len(self.array)
    #     count = [0] * 10

    #     for num in self.array:
    #         index = (num // exp) % 10
    #         count[index] += 1

    #     for i in range(1, 10):
    #         count[i] += count[i - 1]

    #     for i in range(len(self.array) - 1, -1, -1):
    #         index = (self.array[i] // exp) % 10
    #         output[count[index] - 1] = self.array[i]
    #         count[index] -= 1

    #         self.drawBars(["red" if x == i else "blue" for x in range(self.numElements)])
    #         QApplication.processEvents()
    #         time.sleep(0.1)

    #     for i in range(len(self.array)):
    #         self.array[i] = output[i]
    #         self.drawBars()
    #         QApplication.processEvents()
    #         time.sleep(0.1)
    def radixSort(self):
        max_val = max(self.array)  # Get the maximum value in the array to determine the number of digits
        exp = 1  # Start with the least significant digit (LSD)
        
        # Run the countingSort for each digit (LSD to MSD)
        while max_val // exp > 0:
            self.countingSort(exp)  # Sort the array by the current digit (exp is the digit place)
            exp *= 10  # Move to the next digit place
        self.drawBars(["green"] * self.numElements) #?????? WORKSSSS


    def countingSort(self, exp):
        output = [0] * len(self.array)  # Output array that will hold the sorted values
        count = [0] * 10  # Count array to store the frequency of digits (0-9)

        # Count the occurrences of each digit
        for num in self.array:
            index = (num // exp) % 10  # Get the digit at the current place value
            count[index] += 1

        # Update the count array so that each element at each index holds the sum of previous counts
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array by placing the elements in the correct order
        for i in range(len(self.array) - 1, -1, -1):  # Traverse the array in reverse order
            num = self.array[i]
            index = (num // exp) % 10  # Get the digit at the current place value
            output[count[index] - 1] = num  # Place the element in the output array
            count[index] -= 1  # Decrease the count of the digit

            # Visualize the process: highlight the element being processed
            self.drawBars(["red" if x == i else "blue" for x in range(self.numElements)])
            QApplication.processEvents()  # Update the GUI
            if not self.waitForResume():  # Pause/Stop condition
                return
            time.sleep(0.1)

        # Copy the sorted elements from the output array back to the original array
        for i in range(len(self.array)):
            self.array[i] = output[i]
            self.drawBars()  # Redraw the bars after each pass
            QApplication.processEvents()
            if not self.waitForResume():  # Pause/Stop condition
                return
            time.sleep(0.1)

    """
    LINEAR SEARCH
    """
    # def linearSearch(self):
    #     target = self.targetElement
    #     for i in range(len(self.array)):
    #         if self.array[i] == target:
    #             self.drawBars(["red" if x == i else "blue" for x in range(self.numElements)])
    #             QApplication.processEvents()
    #             time.sleep(0.5)
    #             return
    #         else:
    #             self.drawBars(["yellow" if x == i else "blue" for x in range(self.numElements)])
    #             QApplication.processEvents()
    #             time.sleep(0.1)
    #     self.drawBars()
    def linearSearch(self):
        target = self.targetElement
        for i in range(len(self.array)):
            if self.isStopped:
                return
            if self.array[i] == target:
                self.drawBars(["red" if x == i else "blue" for x in range(self.numElements)])
                QApplication.processEvents()
                time.sleep(0.5)
                return
            else:
                self.drawBars(["yellow" if x == i else "blue" for x in range(self.numElements)])
                QApplication.processEvents()
                time.sleep(0.1)
            if not self.waitForResume():
                return
        self.drawBars()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())
