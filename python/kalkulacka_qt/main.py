# This Python file uses the following encoding: utf-8
import sys, os
from PySide2.QtCore import QObject, QUrl, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


# Hlavní třída

class MainPy(QObject):
    # Ukončí aplikaci
    @Slot(int)
    def zavrit_app(self, code):
        app.exit(code)

    @Slot(str)
    def tlacitko_stisknuto(self, id):
        print(id)



###


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    # Přidáno
    mainpy = MainPy()
    engine.rootContext().setContextProperty("mainpy", mainpy)
    ###

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
