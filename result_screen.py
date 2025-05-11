from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class ResultScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        title = QLabel("Résultat du test de Ruffier")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        
        self.interpretation_label = QLabel()
        self.interpretation_label.setAlignment(Qt.AlignCenter)
        self.interpretation_label.setWordWrap(True)
        
        restart_button = QPushButton("Recommencer")
        restart_button.clicked.connect(self.restart)
        
        layout.addWidget(title)
        layout.addWidget(self.result_label)
        layout.addWidget(self.interpretation_label)
        layout.addWidget(restart_button)
        
        self.setLayout(layout)

    def update_result(self, p1, p2, p3):
        # Convert 15-second pulse counts to beats per minute
        p1_bpm = p1 * 4
        p2_bpm = p2 * 4
        p3_bpm = p3 * 4
        
        # Calculate Ruffier index
        ruffier_index = (p1_bpm + p2_bpm + p3_bpm - 200) / 10
        
        # Display results
        self.result_label.setText(
            f"Pouls au repos (P1): {p1} (soit {p1_bpm} bpm)\n"
            f"Pouls après effort (P2): {p2} (soit {p2_bpm} bpm)\n"
            f"Pouls après 1 minute de récupération (P3): {p3} (soit {p3_bpm} bpm)\n\n"
            f"Indice de Ruffier: {ruffier_index:.2f}"
        )
        
        # Interpret the result
        interpretation = self.interpret_ruffier_index(ruffier_index)
        self.interpretation_label.setText(f"Interprétation: {interpretation}")

    def interpret_ruffier_index(self, index):
        if index < 0:
            return "Excellent (Athlétique)"
        elif index < 5:
            return "Très bonne condition physique"
        elif index < 10:
            return "Bonne condition physique"
        elif index < 15:
            return "Condition physique moyenne"
        elif index < 20:
            return "Condition physique insuffisante"
        else:
            return "Mauvaise condition physique"

    def restart(self):
        self.parent.go_to_info_screen()