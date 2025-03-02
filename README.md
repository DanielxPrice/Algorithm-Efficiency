# Comparative Analysis and Visualization of Sorting Algorithms

## Project Overview

This project is a **Comparative Analysis and Visualization of Sorting Algorithms** designed to help users understand the inner workings and efficiency of different sorting algorithms. The application allows users to input an array (either randomly generated or manually entered) and visualize how various algorithms sort the data.

The program leverages **PyQt6** and **PyQt5** for the graphical user interface (GUI) and **matplotlib** for real-time plotting of the sorting process.

### Key Features:
- **Random or Manual Input**: Choose between generating a random array or entering a custom array of integers.
- **Sorting Algorithms**: Visualize the execution of several sorting algorithms (e.g., Bubble Sort, Quick Sort, Merge Sort, etc.).
- **Target Element Search**: Perform a linear search for a target element within the array.
- **Matplotlib Integration**: Visualize the sorting process in real-time using dynamic plots powered by `matplotlib`.

## Sorting Algorithms Used in the Project

This project implements and visualizes the following sorting algorithms:

1. **Bubble Sort**:
   - Bubble Sort compares adjacent elements in an array and swaps them if they are in the wrong order. This process continues until the array is sorted.

2. **Selection Sort**:
   - Selection Sort works by repeatedly finding the smallest (or largest) element from the unsorted part of the list and placing it in the correct position.

3. **Insertion Sort**:
   - Insertion Sort builds the sorted array one element at a time by inserting the current element into the correct position in the already sorted part of the array.

4. **Quick Sort**:
   - Quick Sort is a divide-and-conquer algorithm that picks an element as a pivot and partitions the array into two sub-arrays. The sub-arrays are then sorted recursively.

5. **Merge Sort**:
   - Merge Sort divides the array into two halves, sorts them recursively, and then merges the two sorted halves.

Each algorithm has been implemented with a focus on demonstrating their comparative performance in terms of time complexity and efficiency through visualizations.

## ALGORITHM VISUALIZATION
# Time Complexity Bar Graph
![Array Size: 1212](../images/barGraph.jpg)
# Live Virtualization
![Array Size: 12](../images/liveVirtualization.jpg)
![Array Size: 1212](../images/liveVirtualization2.jpg)

## UI
# Main Page
![Alt text](../images/defaultPage.jpg)
# Random Input
![Alt text](../images/randomInput.jpg)
# Manual Input
![Alt text](../images/manualInput.jpg)


## Technologies Used

- **Python 3.x**
- **PyQt6** and **PyQt5**: For creating the graphical user interface (GUI).
- **matplotlib**: For visualizing the sorting process and array manipulations.
- **Sorting Algorithms**: Various sorting algorithms for comparative analysis.

## Installation

### Prerequisites

- Ensure that you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- pip install PyQt6 matplotlib

### Steps to Set Up the Project

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
