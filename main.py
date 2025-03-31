
import sys

from PyQt6.QtWidgets import QApplication

import MyUIByPyQt6
import userDataJson
from datetime import datetime



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MyUIByPyQt6.MainWindow()
    main_window.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





