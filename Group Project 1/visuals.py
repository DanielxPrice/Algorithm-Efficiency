import sys
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class SortingVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sorting Algorithm Visualizer")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        # Dropdown for sorting algorithm selection
        self.algoSelector = QComboBox(self)
        self.algoSelector.addItems(["Bubble Sort", "Selection Sort", "Insertion Sort"])
        layout.addWidget(self.algoSelector)

        # Buttons
        self.startButton = QPushButton("Start Sorting", self)
        self.startButton.clicked.connect(self.runSorting)
        layout.addWidget(self.startButton)

        self.pauseButton = QPushButton("Pause", self)
        self.pauseButton.clicked.connect(self.togglePause)
        layout.addWidget(self.pauseButton)

        self.endButton = QPushButton("End Sorting", self)
        self.endButton.clicked.connect(self.endSorting)
        layout.addWidget(self.endButton)

        # Matplotlib figure and canvas
        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Sorting control flags
        self.isPaused = False
        self.isStopped = False

        # Generate initial random array
        self.numElements = 20
        self.array = np.random.randint(10, 100, self.numElements)

        self.drawBars()

    def drawBars(self, colors=None):
        """ Updates the bar graph with new data """
        self.ax.clear()
        if colors is None:
            colors = ["cyan"] * self.numElements  # Default color

        self.ax.bar(range(len(self.array)), self.array, color=colors)
        self.ax.set_title("Sorting Visualization")
        self.canvas.draw()

    def runSorting(self):
        """ Runs the selected sorting algorithm with visualization """
        self.isStopped = False  # Reset stop flag
        selectedAlgo = self.algoSelector.currentText()

        if selectedAlgo == "Bubble Sort":
            self.bubbleSort()
        elif selectedAlgo == "Selection Sort":
            self.selectionSort()
        elif selectedAlgo == "Insertion Sort":
            self.insertionSort()

    def togglePause(self):
        """ Toggles between pausing and resuming sorting """
        self.isPaused = not self.isPaused
        self.pauseButton.setText("Resume" if self.isPaused else "Pause")

    def endSorting(self):
        """ Stops sorting immediately """
        self.isStopped = True
        self.isPaused = False
        self.pauseButton.setText("Pause")  # Reset button text
        self.drawBars()  # Refresh UI

    def waitForResume(self):
        """ Pauses sorting until resumed or stopped """
        while self.isPaused:
            QApplication.processEvents()
            time.sleep(0.1)
            if self.isStopped:
                return False
        return True

    def bubbleSort(self):
        """ Bubble Sort Visualization with Pause/Stop Support """
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - 1 - i):
                if self.isStopped:
                    return

                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.drawBars(["red" if x == j or x == j + 1 else "blue" for x in range(self.numElements)])
                    QApplication.processEvents()
                    time.sleep(0.1)

                if not self.waitForResume():
                    return

        self.drawBars(["green"] * self.numElements)  # Final sorted color

    def selectionSort(self):
        """ Selection Sort Visualization with Pause/Stop Support """
        for i in range(len(self.array)):
            if self.isStopped:
                return

            minIndex = i
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[minIndex]:
                    minIndex = j

            self.array[i], self.array[minIndex] = self.array[minIndex], self.array[i]
            self.drawBars(["red" if x == i or x == minIndex else "blue" for x in range(self.numElements)])
            QApplication.processEvents()
            time.sleep(0.1)

            if not self.waitForResume():
                return

        self.drawBars(["green"] * self.numElements)

    def insertionSort(self):
        """ Insertion Sort Visualization with Pause/Stop Support """
        for i in range(1, len(self.array)):
            if self.isStopped:
                return

            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1

                self.drawBars(["red" if x == j + 1 else "blue" for x in range(self.numElements)])
                QApplication.processEvents()
                time.sleep(0.1)

                if not self.waitForResume():
                    return

            self.array[j + 1] = key

        self.drawBars(["green"] * self.numElements)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())


# import matplotlib.pyplot as plt

# # Sample data
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [10, 24, 36, 18, 30]

# # Create a bar chart
# plt.bar(categories, values, color='blue')

# # Add labels and title
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Sample Bar Graph')

# # Show the graph
# plt.show()
