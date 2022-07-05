import sys
import os


from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from tkinter import messagebox
from PyQt6.QtWidgets import QTableWidgetItem



class Dialogo (QDialog):

    def __init__(self):
        ruta = os.path.dirname (os.path.abspath (__file__)) + r"\..\vista\EditarAsignatura.ui"
        QDialog.__init__ (self)
        uic.loadUi (ruta, self)

        self.pushButton.clicked.connect (self.guardar_cambios)
        self.btnSalir.clicked.connect (self.exit_app)
        self.btnSeleccionar.clicked.connect (self.seleccionar_asignaturas)

    def seleccionar_asignaturas(self):

        if self.checkBox.isChecked ():
            self.lblAsignatura.setText ('Diseño de APPs')
        elif self.checkBox_2.isChecked ():
            self.lblAsignatura.setText ('Simulacion')
        elif self.checkBox_3.isChecked ():
            self.lblAsignatura.setText ('Innovacion')
        elif self.checkBox_4.isChecked ():
            self.lblAsignatura.setText ('Base de Datos')

    def guardar_cambios(self):

       if self.checkBox.isChecked():
            self.tableWidget.setItem(1, 1, QTableWidgetItem (self.lineEdit_2.text()))

       elif self.checkBox_2.isChecked ():
            self.tableWidget.setItem (1, 4, QTableWidgetItem (self.lineEdit_2.text ()))

       elif self.checkBox_3.isChecked ():
            self.tableWidget.setItem (2, 4, QTableWidgetItem (self.lineEdit_2.text ()))

       elif self.checkBox_4.isChecked ():
            self.tableWidget.setItem (3, 4, QTableWidgetItem (self.lineEdit_2.text ()))

    def exit_app(self):
        resultado = messagebox.askquestion ("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            # exit(0)
            quit (0)


if __name__ == '__main__':
    app = QApplication (sys.argv)
    dialogo = Dialogo ()
    dialogo.show ()
    app.exec ()
