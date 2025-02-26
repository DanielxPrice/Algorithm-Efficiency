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

        

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)

        #The dropdown menu for selecting with sorting method you want to use
        self.algoSelector = QComboBox(self)
        self.algoSelector.addItems(["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search"])
        layout.addWidget(self.algoSelector)



        #Our buttons for selection, Start Sorting, Pause, and End Sorting
        self.startButton = QPushButton("Start Sorting", self)
        self.startButton.clicked.connect(self.runSorting)
        layout.addWidget(self.startButton)

        self.pauseButton = QPushButton("Pause", self)
        self.pauseButton.clicked.connect(self.togglePause)
        layout.addWidget(self.pauseButton)

        self.endButton = QPushButton("End Sorting", self)
        self.endButton.clicked.connect(self.endSortingtwo)
        layout.addWidget(self.endButton)



        # Matplotlib figure and canvas
        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        #Control flags
        self.isPaused = False
        self.isStopped = False

        #Generating the initial array
        self.numElements = 20
        self.array = np.random.randint(10, 100, self.numElements)

        self.drawBars()


    #Drawing the bars. :)
    def drawBars(self, colors=None):
        #Updates bars
        self.ax.clear()
        if colors is None:
            colors = ["cyan"] * self.numElements  # Default color

        self.ax.bar(range(len(self.array)), self.array, color=colors)
        self.ax.set_title("Sorting Visualization")
        self.canvas.draw()


    def runSorting(self):
        #Choose which sorting algorithm you like, it'll run with visualization
        self.isStopped = False  # Reset stop flag
        selectedAlgo = self.algoSelector.currentText()

        if selectedAlgo == "Bubble Sort":
            self.bubbleSort()
        elif selectedAlgo == "Merge Sort":
            self.mergeSort()
        elif selectedAlgo == "Quick Sort":
            self.quickSort()
        elif selectedAlgo == "Radix Sort":
            self.radixSort()
        elif selectedAlgo == "Linear Search":
            self.linearSearch()
  


    def togglePause(self):
        self.isPaused = not self.isPaused
        self.pauseButton.setText("Resume" if self.isPaused else "Pause")
# Sean ^
# ___________________________________________________________________________________________________________________________________________________________________________________
# Josephine \/

    def endSortingtwo(self):
        """ 
        stops sorting instantly, resets the pause button, and updates the UI 
        """
        self.isStopped = True
        self.isPaused = False
        self.pauseButton.setText("Pause")
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
    
    """
    BUBBLE SORT
    """
    def bubbleSort(self):
        """
        visualizes bubble sort w/ options to pause/stop sorting process 
        """
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

    """
    MERGE SORT
    """
    def mergeSort(self):
        return


        """
        QUICK SORT
        """
    def quickSort(self):


        """
        RADIX SORT
        """
    def radixSort(self):

        """
        LINEAR SEARCH
        """
    def linearSearch(self):
        return
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())


