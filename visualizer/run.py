from PyQt6.QtWidgets import QApplication
from root import main
import sys

def app():
    runserver = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(runserver.exec())
app()