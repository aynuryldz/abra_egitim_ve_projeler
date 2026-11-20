import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Dersleri"
        self.sol = 0
        self.sag = 0
        self.en = 300
        self.boy = 200

        self.setWindowTitle(self.title)
        self.setGeometry(self.sol, self.sag, self.en, self.boy)
   
        self.tab_app = Tablar(self)#tablar sınıfından nesne oluştururuz
        self.setCentralWidget(self.tab_app)

class Tablar(QWidget):
    def __init__(self,temel=None):
        super(Tablar,self).__init__(temel)#farklı bir şekilde de yazılabilir. super().__init__()iki kısma da parametre gelebilir.
        self.arayuz = QVBoxLayout()

        #tabları oluşturma
        self.tablar = QTabWidget()#sekmeli yapı oluşturur
        self.tab1 = QWidget()#ayrı içerik alanları oluşturur
        self.tab2 = QWidget()
        self.tablar.resize(300,200)

        #tabları isimlendirme
        self.tablar.addTab(self.tab1,"Tab1")
        self.tablar.addTab(self.tab2,"Tab2")

        #tab1 içeriği
        self.tab1.arayuz = QVBoxLayout(self)
        self.button_tab1 = QPushButton("Ben Kimim ?")
        self.tab1.setLayout(self.tab1.arayuz)
        self.tab1.arayuz.addWidget(self.button_tab1)
        self.button_tab1.clicked.connect(self.tiklama1)
        #burada QLabel ile tab1 içinde bir yazı alanı oluşturuyoruz. Butona tıklandığında bu yazı alanına yazı yazdıracağız.
        self.yazi_tab1 = QLabel("")
        self.tab1.arayuz.addWidget(self.yazi_tab1)
        self.button_tab1.clicked.connect(self.tiklama1)
        
        #tab2 içeriği
        self.tab2.arayuz = QVBoxLayout(self)
        self.button_tab2 = QPushButton("Ben Kimim ?")
        self.tab2.arayuz.addWidget(self.button_tab2)
        self.tab2.setLayout(self.tab2.arayuz)
        self.button_tab2.clicked.connect(self.tiklama2)
#tablar ve arayüzü bağlamak için kullandık 
        self.arayuz.addWidget(self.tablar)
        self.setLayout(self.arayuz)

    def tiklama1(self):
        print("Tab1e ait butonsun sen!")
        #QMessageBox.information(self,"Bilgi","Tab1e ait butonsun sen!") # MESAJ KUTUSU OLUŞTURMAK İÇİN KULLANILIR.
        #self.yazi_tab1.setText("Tab1e ait butonsun sen!") #yazı yazdırmak için kullanılır. QLabel ile oluşturduğumuz yazı alanına yazı yazdırır.
    def tiklama2(self):
        print("Tab2ye ait butonsun sen!")
        #QMessageBox.information(self,"Bilgi","Tab2ye ait butonsun sen!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    goster = App()
    goster.show()
    sys.exit(app.exec_())


