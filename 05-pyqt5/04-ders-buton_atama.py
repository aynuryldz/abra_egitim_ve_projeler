import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app=QApplication(sys.argv)
    ekran=QDialog()
    #buton1 düzenlenmesi
    b1=QPushButton(ekran)
    b1.setText("Başlat")
    b1.move(20,20)
    b1.clicked.connect(b1_tiklandi) #buton1 tıklandığında b1_tiklandi fonksiyonu çalışır.
    #buton2 düzenlenmesi
    b2=QPushButton(ekran)
    b2.setText("Durdur")
    b2.move(120,20)
    b2.clicked.connect(b2_tiklandi) #buton2 tıklandığında b2_tiklandi fonksiyonu çalışır.

    #ekran düzenlemesi
    ekran.setGeometry(100,100,300,300)
    ekran.setWindowTitle("Buton Atama İşlemleri")
    ekran.show()
    sys.exit(app.exec_())
def b1_tiklandi():
    print("Birinci butona tıklandı")

def b2_tiklandi():
    print("İkinci butona tıklandı")

if __name__=="__main__":
    window()