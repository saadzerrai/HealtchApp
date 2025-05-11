from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class InfoScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        title = QLabel("Test de Ruffier :")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        info_text = QLabel(
            "Le test de Ruffier est un test simple pour évaluer votre condition physique.\n\n"
            "Instructions:\n"
            "1. Mesurez votre pouls au repos pendant 15 secondes (P1)\n"
            "2. Faites 30 flexions en 45 secondes\n"
            "3. Mesurez votre pouls immédiatement après l'effort pendant 15 secondes (P2)\n"
            "4. Mesurez votre pouls 1 minute après l'effort pendant 15 secondes (P3)\n\n"
            "L'application calculera votre indice de Ruffier et évaluera votre condition physique."
        )
        info_text.setAlignment(Qt.AlignCenter)
        info_text.setWordWrap(True)
        
        start_button = QPushButton("Commencer le test")
        start_button.clicked.connect(self.start_test)
        
        layout.addWidget(title)
        layout.addWidget(info_text)
        layout.addWidget(start_button)
        
        self.setLayout(layout)

    def start_test(self):
        self.parent.go_to_input_screen()