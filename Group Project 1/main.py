'''
Group Project 1
Authors:
Daniel Price
Josephine Choi
Sean Defrank
'''
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor, QPainter
from sortingAlgorithms import Algorithms as myAlgorithms

WIDTH = 1000
HEIGHT = 700

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Project")
        self.setGeometry(100, 100, WIDTH, HEIGHT)
        self.setStyleSheet("background-color: #2E3440;")  # Dark mode background

        # Remove window border
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Variables to track dragging
        self.dragging = False
        self.dragPosition = QPoint()

        # Create close button (Top-right corner)
        self.closeButton = QPushButton("X", self)
        self.closeButton.setStyleSheet("""
            background-color: red;
            color: white;
            font-size: 12px;
            font-weight: bold;
            border-radius: 10px;
            padding: 5px;
        """)
        self.closeButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.closeButton.setFixedSize(45, 20)
        self.closeButton.clicked.connect(self.close)

        # Create the title label
        self.titleLabel = QLabel("Comparative Analysis and Visualization of Sorting Algorithms", self)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setStyleSheet("""
            color: white;
            font-size: 30px;
            font-weight: bold;
            padding: 20px;
        """)

        # Create the selection combo box for Random/Manual input
        self.inputTypeComboBox = QComboBox(self)
        self.inputTypeComboBox.addItems(["Select Input Type", "Random", "Manual"])
        self.inputTypeComboBox.setStyleSheet("""
            background-color: #D8DEE9;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        """)
        self.inputTypeComboBox.currentTextChanged.connect(self.onInputTypeChanged)

        # Create the first text box for random array size (only visible for random)
        self.firstTextBox = QLineEdit(self)
        self.firstTextBox.setPlaceholderText("Enter size of array...")
        self.firstTextBox.setStyleSheet("""
            background-color: #D8DEE9;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        """)

        # Create the lower and upper bound text boxes (only visible for random)
        self.lowerBoundTextBox = QLineEdit(self)
        self.lowerBoundTextBox.setPlaceholderText("Enter lower bound...")
        self.lowerBoundTextBox.setStyleSheet("""
            background-color: #D8DEE9;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        """)

        self.upperBoundTextBox = QLineEdit(self)
        self.upperBoundTextBox.setPlaceholderText("Enter upper bound...")
        self.upperBoundTextBox.setStyleSheet("""
            background-color: #D8DEE9;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        """)

        # Create text boxes for manual input (only visible for manual)
        self.manualInputTextBox = QLineEdit(self)
        self.manualInputTextBox.setPlaceholderText("Enter array (comma-separated)...")
        self.manualInputTextBox.setStyleSheet("""
            background-color: #D8DEE9;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        """)

        self.targetTextBox = QLineEdit(self)
        self.targetTextBox.setPlaceholderText("Enter target for linear search...")
        self.targetTextBox.setStyleSheet("""
            background-color: #D8DEE9;
            border-radius: 5px;
            padding: 8px;
            font-size: 16px;
        """)

        # Create a button to generate the random array or search manually
        self.generateButton = QPushButton("Generate", self)
        self.generateButton.setStyleSheet("""
            background-color: #88C0D0;
            color: black;
            font-size: 18px;
            padding: 12px;
            border-radius: 10px;
        """)

        self.generateButton.clicked.connect(self.onGenerate)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.inputTypeComboBox)
        layout.addWidget(self.firstTextBox)
        layout.addWidget(self.lowerBoundTextBox)
        layout.addWidget(self.upperBoundTextBox)
        layout.addWidget(self.manualInputTextBox)
        layout.addWidget(self.targetTextBox)
        layout.addWidget(self.generateButton)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 40, 20, 20)

        self.setLayout(layout)

        self.onInputTypeChanged(self.inputTypeComboBox.currentText())  # Call to hide/show based on default

    def onInputTypeChanged(self, input_type):
        # Hide or show widgets based on selected input type
        if input_type == "Random":
            self.firstTextBox.show()
            self.lowerBoundTextBox.show()
            self.upperBoundTextBox.show()
            self.manualInputTextBox.hide()
            self.targetTextBox.hide()
        elif input_type == "Manual":
            self.firstTextBox.hide()
            self.lowerBoundTextBox.hide()
            self.upperBoundTextBox.hide()
            self.manualInputTextBox.show()
            self.targetTextBox.show()
        else:
            self.firstTextBox.hide()
            self.lowerBoundTextBox.hide()
            self.upperBoundTextBox.hide()
            self.manualInputTextBox.hide()
            self.targetTextBox.hide()

    '''
    This is where the logic is. onGenerate()

    The rest of the code in the file is ui stuff. 
    The ui is not done yet. We need to redirect to another page and display the visual.
    We can do that with hide() or
    We can probably just open a new window so if the user wants to switch their choices, they just press x.
    We then use matplotlib or pygame as the other window
    We pass in the info to the class using matplotlib or pygame and display in the new window/s
    
    
    '''
    def onGenerate(self):
        input_type = self.inputTypeComboBox.currentText()
        
        if input_type == "Random":
            try:
                # Get values from the UI
                array_size = int(self.firstTextBox.text())
                lower_bound = int(self.lowerBoundTextBox.text())
                upper_bound = int(self.upperBoundTextBox.text())
                print(f"Generating random array with size {array_size}, lower bound {lower_bound}, and upper bound {upper_bound}")

                # Create an instance of the algorithms class with random values
                random_algo = myAlgorithms(lower_bound, upper_bound, array_size, [], input_type="Random")
                random_algo.random_choice()
                print(f"[DEBUG] Random array before sorting: {random_algo.random_array}")
                random_algo.run()            

            except ValueError:
                print("Please enter valid integer values.")

        elif input_type == "Manual":
            try:
                # Get manual input (comma-separated values)
                manual_array = list(map(int, self.manualInputTextBox.text().split(',')))
                target = int(self.targetTextBox.text())
                # print(f"Manual array: {manual_array}, Target: {target}")

                # Create an instance of the algorithms class with the manual values
                manual_algo = myAlgorithms(0, 0, 0, manual_array, target, input_type)
                manual_algo.run()
            except ValueError:
                print("Please enter valid values for the array and target.")

        else:
            print("Please select a valid input type (Random or Manual).")


    # Enable dragging of the borderless window by clicking the title bar
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and event.pos().y() < 40:
            self.dragging = True
            self.dragPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.dragging and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.dragging = False

    # Paint event to customize the title bar
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw a custom title bar (drag bar)
        painter.setBrush(QColor("#4C566A"))  # Set color for the drag bar
        painter.drawRect(0, 0, self.width(), 30)  # Draw the title bar (top part of the window)

        # Draw close button in custom position
        self.closeButton.move(self.width() - 50, 5)  # Move close button to the right top corner

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

