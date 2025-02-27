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
   

        # Attempt at passing data
        if len(sys.argv) != 6:
            print("Usage: visuals.py <arraySize> <lowerBound> <upperBound>")
            return

        try:
            # Read input values from command-line arguments
            self.arraySize = int(sys.argv[1])
            self.lowerBound = int(sys.argv[2])
            self.upperBound = int(sys.argv[3])
            self.manualArray = list(map(int, sys.argv[4].split(',')))
            self.permManualArray = list(map(int, sys.argv[4].split(',')))
            #manualArray = int(sys.argv[4])
            self.targetElement =  int(sys.argv[5])
            #print(manualArray)
            # Display received values (replace this with actual visualization logic)
            print(f"Received values: arraySize={self.arraySize}, lowerBound={self.lowerBound}, upperBound={self.upperBound}, manualArray={self.manualArray}, targetElement={self.targetElement}")
            print(f"2 This is manual array {self.manualArray}")
            # TODO: Implement sorting visualization logic using the received values

        except ValueError:
            print("Invalid input. Please ensure all inputs are integers.")


        


        
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

        print(f"This is the array {self.array} of type: {type(self.array)}")
        self.drawBars()







    def drawBars(self, colors=None):
        self.ax.clear()
        if colors is None:
            colors = ["cyan"] * self.numElements
        self.ax.bar(range(len(self.array)), self.array, color=colors)
        self.ax.set_title("Sorting Visualization")
        self.canvas.draw()

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

    def togglePause(self):
        self.isPaused = not self.isPaused
        self.pauseButton.setText("Resume" if self.isPaused else "Pause")

    def endSorting(self):
        """ 
        stops sorting instantly, resets the pause button, and updates the UI 
        """
        self.isStopped = True
        self.isPaused = False
        self.pauseButton.setText("Pause")
        self.drawBars()
        
    # def resetSorting(self):
    #     self.isStopped = True
    #     self.isPaused = False
    #     self.pauseButton.setText("Pause")
    #     self.drawBars()

    def resetSorting(self):
        """ Resets the sorting visualizer to its original state """
        self.isStopped = True
        self.isPaused = False
        self.pauseButton.setText("Pause")

        if self.arraySize == 0:  
            self.array = self.permManualArray.copy() 
        else:  
            self.array = [random.randint(self.lowerBound, self.upperBound) for _ in range(self.numElements)]

        self.drawBars()


    def waitForResume(self):
        """
        pauses the sorting until it resumes/stops
        """
        while self.isPaused:
            QApplication.processEvents()
            time.sleep(0.1)
            if self.isStopped:
                return False
        return True


    def bubbleSort(self):
        """
        visualizes bubble sort w/ options to pause/stop sorting process 
        """
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

                # Check if the algorithm should pause/stop
                if not self.waitForResume():
                    return

        self.drawBars(["green"] * self.numElements)



    def mergeSort(self, left, right):
        if left < right:
            if self.isStopped:
                return
            
            mid = (left + right) // 2
            
            # Recursively sort the left and right halves
            self.mergeSort(left, mid)
            self.mergeSort(mid + 1, right)
            
            # Visualize the merge process (merge step without actually merging)
            self.visualizeMerge(left, mid, right)
            
            # Check if the algorithm should pause/stop
            if not self.waitForResume():
                return

    def visualizeMerge(self, left, mid, right):
        """
        Visualizes the merge process where elements are ordered from smallest to largest
        during the merge step, without changing the actual array.
        """
        if self.isStopped:
            return
        
        # Create temporary arrays for the left and right halves
        left_half = self.array[left:mid+1]
        right_half = self.array[mid+1:right+1]
        
        # Temporary merged array (this is what we would visualize)
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
        
        # Visualize the "merged" array
        merged_index = 0
        for k in range(left, right + 1):
            # Color elements from the merged array as "yellow"
            if merged_index < len(merged):
                self.array[k] = merged[merged_index]
                merged_index += 1

        # Update the visualization with the current state of the array
        self.drawBars(["yellow" if left <= x <= right else "blue" for x in range(self.numElements)])
        
        QApplication.processEvents()
        time.sleep(0.1)
        
        # Check if the algorithm should pause/stop
        if not self.waitForResume():
            return
        
        # Visualize the final sorted portion as green
        self.drawBars(["green" if left <= x <= right else "blue" for x in range(self.numElements)])
        QApplication.processEvents()
        time.sleep(0.1)



    def quickSort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            if pivot is None:
                print(f"Error: partition returned None. low={low}, high={high}")
                return  # Avoid recursion if partition fails & recursively sort the two halves
            self.quickSort(low, pivot - 1)
            self.quickSort(pivot + 1, high)

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
    Pause doesnt work
    """
    def radixSort(self):
        max_val = max(self.array)
        exp = 1
        while max_val // exp > 0:
            self.countingSort(exp)
            exp *= 10

    def countingSort(self, exp):
        output = [0] * len(self.array)
        count = [0] * 10

        for num in self.array:
            index = (num // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(self.array) - 1, -1, -1):
            index = (self.array[i] // exp) % 10
            output[count[index] - 1] = self.array[i]
            count[index] -= 1

            self.drawBars(["red" if x == i else "blue" for x in range(self.numElements)])
            QApplication.processEvents()
            time.sleep(0.1)

        for i in range(len(self.array)):
            self.array[i] = output[i]
            self.drawBars()
            QApplication.processEvents()
            time.sleep(0.1)


    def linearSearch(self):
        target = self.targetElement
        for i in range(len(self.array)):
            if self.array[i] == target:
                self.drawBars(["red" if x == i else "blue" for x in range(self.numElements)])
                QApplication.processEvents()
                time.sleep(0.5)
                return
            else:
                self.drawBars(["yellow" if x == i else "blue" for x in range(self.numElements)])
                QApplication.processEvents()
                time.sleep(0.1)
        self.drawBars()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())
