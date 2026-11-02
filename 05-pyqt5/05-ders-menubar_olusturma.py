import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication,QAction,QPushButton,QMenu,QMenuBar
# class window(QMainWindow):#bu şekilde de yazılabilirdi.
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("PyQt5 Dersleri")
#         self.setGeometry(10, 10, 640, 400)#değerleri değişken olarak saklamak yerine direk yazdık
#         anaMenu = self.menuBar()
#         fileMenu = anaMenu.addMenu("File")
#         editMenu = anaMenu.addMenu("Edit")
#         viewMenu = anaMenu.addMenu("View")

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslik = "PyQt5 Dersleri"
        self.sol=10
        self.ust=10
        self.en=640
        self.boy=400
        self.arayüz()
#QAction ile çalıştırılabilecek işlemler oluşturulur.çıkış yapmak gibi    def arayüz(self):

    def arayüz(self):
        self.setWindowTitle(self.baslik)#önceden belirlenen değerleri alırız.
        self.setGeometry(self.sol, self.ust, self.en, self.boy)

        anaMenu = self.menuBar() #menü çubuğu oluşturur.
        fileMenu = anaMenu.addMenu("File") #anaMenu çubuğuna File adlı bir menü ekler.Oluşan menüyü fileMenu adıyla saklar.       
        editMenU = anaMenu.addMenu("Edit")
        viewMenu = anaMenu.addMenu("View")
        newProject = fileMenu.addMenu('New')
        icerik=newProject.addAction("Yeni proje oluşturuldu.")
        icerik.triggered.connect(self.tiklandi)

        cikisButonu = QAction(QIcon("exit.png"), "Çıkış", self) #çıkış butonu oluşturur.
        cikisButonu.setShortcut("Ctrl+Q") #çıkış butonuna kısayol atar.
        cikisButonu.setStatusTip("Uygulamayı kapat.") 
        cikisButonu.triggered.connect(self.close) #çıkış butonuna tıklandığında pencereyi kapatır.
        fileMenu.addAction(cikisButonu) #fileMenu menüsüne çıkış butonunu ekler.
    def tiklandi(self):
        print("tıklandı")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ekran = window()
    ekran.show()
    sys.exit(app.exec_())