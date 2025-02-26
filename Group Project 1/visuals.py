# import sys
# import random
# import time
# import numpy as np
# import matplotlib.pyplot as plt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox
# from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

# class SortingVisualizer(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Sorting Algorithm Visualizer")
#         self.setGeometry(100, 100, 800, 600)

        

#         self.centralWidget = QWidget(self)
#         self.setCentralWidget(self.centralWidget)
#         layout = QVBoxLayout(self.centralWidget)

#         #The dropdown menu for selecting with sorting method you want to use
#         self.algoSelector = QComboBox(self)
#         self.algoSelector.addItems(["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search"])
#         layout.addWidget(self.algoSelector)



#         #Our buttons for selection, Start Sorting, Pause, and End Sorting
#         self.startButton = QPushButton("Start Sorting", self)
#         self.startButton.clicked.connect(self.runSorting)
#         layout.addWidget(self.startButton)

#         self.pauseButton = QPushButton("Pause", self)
#         self.pauseButton.clicked.connect(self.togglePause)
#         layout.addWidget(self.pauseButton)

#         self.endButton = QPushButton("End Sorting", self)
#         self.endButton.clicked.connect(self.endSortingtwo)
#         layout.addWidget(self.endButton)



#         # Matplotlib figure and canvas
#         self.figure, self.ax = plt.subplots(figsize=(8, 4))
#         self.canvas = FigureCanvas(self.figure)
#         layout.addWidget(self.canvas)

#         #Control flags
#         self.isPaused = False
#         self.isStopped = False

#         #Generating the initial array
#         self.numElements = 20
#         self.array = np.random.randint(10, 100, self.numElements)

#         self.drawBars()


#     #Drawing the bars. :)
#     def drawBars(self, colors=None):
#         #Updates bars
#         self.ax.clear()
#         if colors is None:
#             colors = ["cyan"] * self.numElements  # Default color

#         self.ax.bar(range(len(self.array)), self.array, color=colors)
#         self.ax.set_title("Sorting Visualization")
#         self.canvas.draw()


#     def runSorting(self):
#         #Choose which sorting algorithm you like, it'll run with visualization
#         self.isStopped = False  # Reset stop flag
#         selectedAlgo = self.algoSelector.currentText()

#         if selectedAlgo == "Bubble Sort":
#             self.bubbleSort()
#         elif selectedAlgo == "Merge Sort":
#             self.mergeSort()
#         elif selectedAlgo == "Quick Sort":
#             self.quickSort()
#         elif selectedAlgo == "Radix Sort":
#             self.radixSort()
#         elif selectedAlgo == "Linear Search":
#             self.linearSearch()
  


#     def togglePause(self):
#         self.isPaused = not self.isPaused
#         self.pauseButton.setText("Resume" if self.isPaused else "Pause")
# # Sean ^
# # ___________________________________________________________________________________________________________________________________________________________________________________
# # Josephine \/

#     def endSortingtwo(self):
#         """ 
#         stops sorting instantly, resets the pause button, and updates the UI 
#         """
#         self.isStopped = True
#         self.isPaused = False
#         self.pauseButton.setText("Pause")
#         self.drawBars()

#     def waitForResume(self):
#         """
#         pauses the sorting until it resumes/stops
#         """
#         while self.isPaused:
#             QApplication.processEvents()
#             time.sleep(0.1)
#             if self.isStopped:
#                 return False
#         return True
    
#     """
#     BUBBLE SORT
#     """
#     def bubbleSort(self):
#         """
#         visualizes bubble sort w/ options to pause/stop sorting process 
#         """
#         for i in range(len(self.array) - 1):
#             for j in range(len(self.array) - 1 - i):
#                 if self.isStopped:
#                     return

#                 if self.array[j] > self.array[j + 1]:
#                     self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
#                     self.drawBars(["red" if x == j or x == j + 1 else "blue" for x in range(self.numElements)])
#                     QApplication.processEvents()
#                     time.sleep(0.1)

#                 if not self.waitForResume():
#                     return

#         self.drawBars(["green"] * self.numElements)  # Final sorted color

#     """
#     MERGE SORT
#     """
#     def mergeSort(self):
#         return


#         """
#         QUICK SORT
#         """
#     def quickSort(self):


#         """
#         RADIX SORT
#         """
#     def radixSort(self):

#         """
#         LINEAR SEARCH
#         """
#     def linearSearch(self):
#         return
    


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SortingVisualizer()
#     window.show()
#     sys.exit(app.exec())

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class SortingVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        
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

        self.numElements = 20
        self.array = np.random.randint(10, 100, self.numElements)
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
        
    def resetSorting(self):
        self.isStopped = True
        self.isPaused = False
        self.pauseButton.setText("Pause")
        self.array = np.random.randint(10, 100, self.numElements)
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
            mid = (left + right) // 2
            self.mergeSort(left, mid)
            self.mergeSort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        leftArray = self.array[left:mid+1]
        rightArray = self.array[mid+1:right+1]
        
        i = j = 0
        k = left

        self.drawBars(["yellow" if x >= left and x <= right else "blue" for x in range(self.numElements)])

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                self.array[k] = leftArray[i]
                i += 1
            else:
                self.array[k] = rightArray[j]
                j += 1
            k += 1
            self.drawBars(["yellow" if x >= left and x <= right else "blue" for x in range(self.numElements)])
            QApplication.processEvents()
            time.sleep(0.1)

        while i < len(leftArray):
            self.array[k] = leftArray[i]
            i += 1
            k += 1
            self.drawBars(["yellow" if x >= left and x <= right else "blue" for x in range(self.numElements)])
            QApplication.processEvents()
            time.sleep(0.1)

        while j < len(rightArray):
            self.array[k] = rightArray[j]
            j += 1
            k += 1
            self.drawBars(["yellow" if x >= left and x <= right else "blue" for x in range(self.numElements)])
            QApplication.processEvents()
            time.sleep(0.1)

        self.drawBars(["green"] * self.numElements)



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
        target = np.random.choice(self.array)
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
