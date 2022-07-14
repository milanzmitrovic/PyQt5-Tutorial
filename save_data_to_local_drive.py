import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.options = (
            # 'Get File Name',
            # 'Get File Names',
            'Please choose location for saving json file with extracted routes.',
            # 'Save File Name'
        )

        self.combo = QComboBox()
        self.combo.addItems(self.options)
        layout.addWidget(self.combo)

        btn = QPushButton('Choose location')
        btn.clicked.connect(self.launchDialog)
        layout.addWidget(btn)

    def launchDialog(self):
        option = self.options.index(self.combo.currentText())

        if option == 0:
            self.getDirectory()

    def getDirectory(self):
        response = QFileDialog.getExistingDirectory(
            self,
            caption='Select a folder'
        )
        print(response)
        
        # Here should come logic for creating and saving json file with data
        
        return response


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

