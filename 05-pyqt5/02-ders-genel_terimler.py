import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):#knedi pencere sınıfımızı oluşturuyoruz.
    def __init__(self, parent=None):#başlangıçta çalışan metod.
        #super() ile QWidget sınıfının __init__ metodunu çağırıyoruz. Bu, pencerenin temel özelliklerini ve işlevselliğini başlatır.kendi sınıfımızın dayandığı süt sınıfın metodlarına ulaşmamızı sağlar.
        super().__init__(parent) # Önce QWidget'in temel pencere altyapısını hazırla.
        self.resize(800, 400)
        self.setWindowTitle("PyQt5 Dersleri")
        self.yazi = QLabel(self) #nesneye ait bir özellik oluştururuz.
        self.yazi.setText("Koddunyam.net!")
        font = QFont() #pencereye ait olarak saklanmaz.self kullanılmamıştır o yüzden.
        font.setFamily("Arial")
        font.setPointSize(16)
        self.yazi.setFont(font)
        self.yazi.adjustSize()
        self.yazi.move(50, 20)
        
        # Kullanıcının yazı yazacağı kutu tanımlamak için kullanılır.
        self.ad_kutusu = QLineEdit(self) #tek satırlık giriş alır.
        self.ad_kutusu.setGeometry(20, 50, 200, 30)
        self.ad_kutusu.setPlaceholderText("Örnek: Aynur") #kutu boşken soluk bir yardımcı yazı gösterir.
        
        # Kullanıcının tıklayacağı buton oluşturulur QPushButton ile.
        self.buton = QPushButton("Selam ver", self)
        self.buton.setGeometry(20, 90, 100, 30)
        
        #seçeneklerden birini seçmek için kullanılır.
        self.ogrenci = QRadioButton("Öğrenci", self)
        self.ogrenci.move(20, 150)
        self.mezun = QRadioButton("Mezun", self)
        self.mezun.move(20, 180)

        #birden fazla seçeneği işaretlemek için kullanılır.
        self.python = QCheckBox("Python", self)
        self.python.move(20, 200)
        self.java = QCheckBox("Java", self)
        self.java.move(20, 220)

        #kullanıcının seçim yapacağı açılır kutu oluşturmak için kullanılır.
        self.sehir = QComboBox(self)
        self.sehir.setGeometry(20, 250, 180, 30)
        self.sehir.addItems(["Ankara", "Sivas", "Sakarya"])#listedeki seçenekleri listeler.
        
        #sayı seçmek için kullanılır.
        self.adet = QSpinBox(self)
        self.adet.setGeometry(20, 290, 100, 30)
        self.adet.setRange(1, 20)#max min değer seçeneği
        self.adet.setValue(1)#başlandıç değeri
        
        #kaydırma çubuğu oluşturmak için kullanılır.
        self.ses = QSlider(Qt.Horizontal, self)
        self.ses.setGeometry(20, 330, 200, 30)
        self.ses.setRange(0, 100)
        self.ses.setValue(50)
        
        #çok satırlı yazı alanı oluşturmak için kullanılır.
        self.not_alani = QTextEdit(self)
        self.not_alani.setGeometry(20, 380, 250, 120)
        self.not_alani.setPlaceholderText("Notunuzu yazınız...") 
def main():
    app = QApplication(sys.argv)
    ekran = window()
    ekran.show()
    sys.exit(app.exec_())

if __name__ == "__main__":    
    main()