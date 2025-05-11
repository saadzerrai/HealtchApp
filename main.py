import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from info_screen import InfoScreen
from input_screen import InputScreen
from result_screen import ResultScreen

class RuffierTestApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.user_data = {}

    def initUI(self):
        self.setWindowTitle('Test de Ruffier : V0.0.1 by @saadzerrai')
        self.setGeometry(300, 300, 600, 400)

        # Create screens
        self.info_screen = InfoScreen(self)
        self.input_screen = InputScreen(self)
        self.result_screen = ResultScreen(self)

        # Add screens to stacked widget
        self.addWidget(self.info_screen)
        self.addWidget(self.input_screen)
        self.addWidget(self.result_screen)

        # Start with info screen
        self.setCurrentIndex(0)

    def go_to_input_screen(self):
        self.setCurrentIndex(1)

    def go_to_result_screen(self, p1, p2, p3):
        self.user_data['p1'] = p1
        self.user_data['p2'] = p2
        self.user_data['p3'] = p3
        self.result_screen.update_result(p1, p2, p3)
        self.setCurrentIndex(2)

    def go_to_info_screen(self):
        self.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RuffierTestApp()
    ex.show()
    sys.exit(app.exec_())