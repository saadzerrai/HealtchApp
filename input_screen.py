from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QSpinBox, QFormLayout)
from PyQt5.QtCore import Qt

class InputScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        title = QLabel("Saisie des mesures")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        form_layout = QFormLayout()
        
        # P1 input
        self.p1_input = QSpinBox()
        self.p1_input.setRange(0, 50)
        self.p1_input.setSingleStep(1)
        form_layout.addRow("P1 (pouls au repos pour 15 secondes):", self.p1_input)
        
        # P2 input
        self.p2_input = QSpinBox()
        self.p2_input.setRange(0, 50)
        self.p2_input.setSingleStep(1)
        form_layout.addRow("P2 (pouls après effort pour 15 secondes):", self.p2_input)
        
        # P3 input
        self.p3_input = QSpinBox()
        self.p3_input.setRange(0, 50)
        self.p3_input.setSingleStep(1)
        form_layout.addRow("P3 (pouls 1 minute après effort pour 15 secondes):", self.p3_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        back_button = QPushButton("Retour")
        back_button.clicked.connect(self.go_back)
        
        calculate_button = QPushButton("Calculer")
        calculate_button.clicked.connect(self.calculate_result)
        
        button_layout.addWidget(back_button)
        button_layout.addWidget(calculate_button)
        
        layout.addWidget(title)
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

    def go_back(self):
        self.parent.go_to_info_screen()

    def calculate_result(self):
        p1 = self.p1_input.value()
        p2 = self.p2_input.value()
        p3 = self.p3_input.value()
        
        self.parent.go_to_result_screen(p1, p2, p3)