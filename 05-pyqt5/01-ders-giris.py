import sys 
from PyQt5.QtCore import * #zamanlayıcı,sinyal ve temel altyapı sınıfları
from PyQt5.QtGui import * #yazi tipi,rengi görsel işlemler
from PyQt5.QtWidgets import * #pencere,buton,etiket gibi arayüz elemanları
#burada hazır qwdidget nesnesi oluşturduk ve pencerenin ayarlarını fonksiyonla yazdık.
#def window():
    # #önce qapplication sınıfından bir nesne oluşturulur.Bu nesne uygulamanın çalışması için gerekli altyapıyı sağlar.
    # app = QApplication(sys.argv)  #sys.argv program başlatılırken verilen bilgileri taşır.
    # w = QWidget()
    # yazi = QLabel(w) #ekranda yazı veya resim göstermek için kullanılan arayüz elemanı
    # yazi.setText("Kod dünyam.net!")
    # w.setGeometry(100, 100, 200, 50) #(ekranın neresinden çıksın)pencerenin konumu
    # yazi.move(50, 20) #yazının konumu
    # w.setWindowTitle("PyQt5 Dersleri")
    # w.show() #pencerenin görünmesini sağlar
    # sys.exit(app.exec_()) #app.exec olay döngüsünü başlatır.uygulama bitene kadar çalışmaya devam eder.sys çıkış kodları programdan çıkışı gerçekleştirir.

# if __name__ == "__main__":#dosya doğrudan çağırıldıysa çalıştırılır.
#     window()

#burada qwidgettan türeyen kendi pencere sınıfımızı yazdık.
class window(QWidget):#knedi pencere sınıfımızı oluşturuyoruz.
    def __init__(self, parent=None):#başlangıçta çalışan metod.
        #super() ile QWidget sınıfının __init__ metodunu çağırıyoruz. Bu, pencerenin temel özelliklerini ve işlevselliğini başlatır.kendi sınıfımızın dayandığı süt sınıfın metodlarına ulaşmamızı sağlar.
        super().__init__(parent) # Önce QWidget'in temel pencere altyapısını hazırla.
        self.resize(200, 50)
        self.setWindowTitle("PyQt5 Dersleri")
        self.yazi = QLabel(self) #nesneye ait bir özellik oluştururuz.
        self.yazi.setText("Koddunyam.net!")
        font = QFont() #pencereye ait olarak saklanmaz.self kullanılmamıştır o yüzden.
        font.setFamily("Arial")
        font.setPointSize(16)
        self.yazi.setFont(font)
        self.yazi.adjustSize()
        self.yazi.move(50, 20)
def main():
    app = QApplication(sys.argv)
    ekran = window()
    ekran.show()
    sys.exit(app.exec_())

if __name__ == "__main__":    
    main()