# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets #modulleri dahil ettik
import datetime
from PyQt5.QtWidgets import QFileDialog,QMainWindow
import datetime
import os
import sys
import time
import webbrowser
import sqlite3
from PIL import Image
import cv2



class Ui_urunbilgileri(object): # sınıfımız açıyoruz
    def setupUi(self, urunbilgileri): # bir fonksiyon tanımlayıp ana penceremizin nesne adınız yazıyoruz
        urunbilgileri.setObjectName("urunbilgileri") # fonksiyonumuzun nesne adını yazıyoruz.
        urunbilgileri.setFixedSize(870,320) # pencere boyutunu değişmeini engelledik. Kullanıcı tarafından değiştirilemez. Teklif dahi edilemez :)
        icon = QtGui.QIcon() # penceremize bir ikon eklemek için ikon oluşturma fonksiyonunu bir değişkene atıyoruz
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # iconumu belirleyip ekliyoruz.
        urunbilgileri.setWindowIcon(icon) #urunbilgieri adını verdiğimiz pencermize belirlediğimiz ikonu ekliyoruz
        urunbilgileri.setStyleSheet("background-color: rgb(197, 197, 197);") #burda herhangi bir işlem yapmadık qt designer ile yapıldığı için default olarak geldi.
        self.line = QtWidgets.QFrame(urunbilgileri) # penceremize düzen için uzun çizgileri ekledik
        self.line.setGeometry(QtCore.QRect(190, 20, 20, 281)) # daha sonra pencereye eklenen uzun çizgileri konumlarını ve boyutlarını belirledik
        self.line.setFrameShape(QtWidgets.QFrame.VLine) # eklenen uzun çizgilerin dikey olmasını istedik (VLİNE) =DİKEY UZUN ÇİZGİLER
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line") # daha sonra ise eklediğimiz uzun nesnemize line diye isim verdik (objectname = nesne adı)
        self.line_3 = QtWidgets.QFrame(urunbilgileri)# yine bir çizgi ekledik ve özellikleri yukarıdaki ile hemen hemen aynı bir kaç değişiklik olmuş olabilir.
        self.line_3.setGeometry(QtCore.QRect(20, 290, 181, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(urunbilgileri)
        self.line_4.setGeometry(QtCore.QRect(10, 30, 20, 271))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_2 = QtWidgets.QLabel(urunbilgileri) # burda pencerimize bir label(etiket) ekledik buraya istediğimiz yazı,rsim veya herhangi bir şeyi ekleyebiliriz.
        self.label_2.setGeometry(QtCore.QRect(20, 50, 171, 111)) # eklenen labelin boyutlarını belirledik. SETGEOMETRİ İLE BOYUT VE KONUM BELİRLİYORUZ
        self.label_2.setStyleSheet("image: url(:/newPrefix/hombre.png);") # labelimize bir foto ekledik
        self.label_2.setText("") # text(yazı) alnını boş bıraktık istersek foto ve yazıyı aynı labelde barındaırabiliriz.
        self.label_2.setObjectName("label_2") # labelimiz isim verdik
        self.label_3 = QtWidgets.QLabel(urunbilgileri) # burda yeni bir label oluşturduk özellikleri hemne hemen yine aynı :)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(urunbilgileri)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 31, 16))
        self.label_4.setObjectName("label_4")
        self.url = QtWidgets.QPushButton(urunbilgileri)
        self.url.setGeometry(QtCore.QRect(30, 270, 35, 28))
        self.url.setText("")
        url_icon = QtGui.QIcon()
        url_icon.addPixmap(QtGui.QPixmap(":/newPrefix/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.url.setIcon(url_icon)
        self.url.setIconSize(QtCore.QSize(38, 41))
        self.url.setObjectName("url")
        self.url.clicked.connect(self.settings)
        self.label_5 = QtWidgets.QLabel(urunbilgileri)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 51, 16))
        self.label_5.setObjectName("label_5")
        self.line_6 = QtWidgets.QFrame(urunbilgileri)  # burda hatırlarssanız uzun çizgileri eklemiştik burda yine ekledik. yatay olarak ekleme yaptık
        self.line_6.setGeometry(QtCore.QRect(340, 10, 511, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_6 = QtWidgets.QLabel(urunbilgileri)
        self.label_6.setGeometry(QtCore.QRect(280, 10, 61, 16))
        font = QtGui.QFont() # label_6 ya ani butonumuza font belirlemek için font fonksiyonunun bir değişkene atadık.
        font.setBold(True) # kalın olmasını istediğimiz için true değerini verdik altı çizili olmasını isteseydil setUnderline(True) gibi bir şey yapacaktık
        font.setWeight(75) #boyutunu yazdık
        self.label_6.setFont(font) # burda aşağı kısımda belirteceğiz buton değerlerine yukarı kısımda belirttiğimiz font değerlerini atayacağız.
        self.label_6.setObjectName("label_6")
        self.button_back = "background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));"
        self.pushButton = QtWidgets.QPushButton(urunbilgileri) # penceremize bir buton ekledik
        self.pushButton.setGeometry(QtCore.QRect(700, 240, 131, 51)) # butonumuzun boyutunu ve konumunu ayarlardık
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Se.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(self.button_back)
        self.pushButton.clicked.connect(self.ur_goster)  # bu butona basıldığında yan ara butonuna basıldığında aşağı kısımda yazdığımız fonksiyonu çağırıyoruz
        self.pushButton_2 = QtWidgets.QPushButton(urunbilgileri)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 240, 131, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("selection-background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        icon2 = QtGui.QIcon() # butonumuza bir ikon eklemek için ikon fonksiyonunu bir değişkene atadık
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/640.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2) # butonumuza belirtilen ikonu ekledik.
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25)) # ikon boyutunu belirledil
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(self.button_back)
        self.pushButton_2.clicked.connect(self.urun_penceresi_goster)
        self.pushButton_3 = QtWidgets.QPushButton(urunbilgileri)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 240, 131, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/sil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(self.button_back)
        self.pushButton_3.clicked.connect(self.stok_sil_goster)
        self.pushButton_4 = QtWidgets.QPushButton(urunbilgileri)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 240, 131, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.update_goster)
        self.pushButton_4.setStyleSheet(self.button_back)
        self.line_8 = QtWidgets.QFrame(urunbilgileri)
        self.line_8.setGeometry(QtCore.QRect(840, 20, 20, 281))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_7 = QtWidgets.QLabel(urunbilgileri)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(20, 300, 281, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(urunbilgileri)
        self.label_8.setGeometry(QtCore.QRect(300, 30, 531, 181))
        self.label_8.setStyleSheet("image: url(:/newPrefix/logo.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(urunbilgileri)
        self.label_9.setGeometry(QtCore.QRect(100, 190, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(urunbilgileri)
        self.label_10.setGeometry(QtCore.QRect(100, 220, 72, 25))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(urunbilgileri)
        self.label_11.setGeometry(QtCore.QRect(100, 250, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(urunbilgileri)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(urunbilgileri)
        self.line_2.setGeometry(QtCore.QRect(270, 290, 581, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(urunbilgileri)
        self.line_5.setGeometry(QtCore.QRect(260, 20, 20, 281))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_7 = QtWidgets.QFrame(urunbilgileri)
        self.line_7.setGeometry(QtCore.QRect(100, 10, 101, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.zaman = datetime.datetime.now()
        self.saat = datetime.datetime.strftime(self.zaman ,"Tarih:%x\nSaat:%X")

        self.retranslateUi(urunbilgileri) # aşağı kısımda yazdğımız fonksiyonu penceremize ekledk
        QtCore.QMetaObject.connectSlotsByName(urunbilgileri)

    def retranslateUi(self, urunbilgileri): # yukarı yazdığımız butın ve label(etiket)lere yazılarını eklemek için ayrı bir fonksiyon tanımladık
        _translate = QtCore.QCoreApplication.translate
        urunbilgileri.setWindowTitle(_translate("urunbilgileri", "STOK TAKİP V.1.0")) # ana penceremizin başlığını belirledik
        self.label_3.setText(_translate("urunbilgileri", "Kullanıcı adı:")) # label_3 e yazmak istediğimiz yazıyı ekledik
        self.label_4.setText(_translate("urunbilgileri", "Yetki:"))
        self.label_5.setText(_translate("urunbilgileri", "Giriş Tarihi:"))
        self.label_6.setText(_translate("urunbilgileri", "İŞLEMLER"))
        self.pushButton.setText(_translate("urunbilgileri", "STOK ARA")) # butonların üzerinde yazmak istediğimiz yazıları ekledik baştaki urunbilgileri yazısı ise ana penceremizin nesne adı oluyor
        self.pushButton_2.setText(_translate("urunbilgileri", "STOK EKLE"))
        self.pushButton_3.setText(_translate("urunbilgileri", "STOK SİL"))
        self.pushButton_4.setText(_translate("urunbilgileri", "STOK GÜNCELLE"))
        self.label_7.setText(_translate("urunbilgileri", "by Ubeyde© Coded 2018 -- All Rights Reserved"))
        self.label_9.setText(_translate("urunbilgileri", ""))
        self.label_10.setText(_translate("urunbilgileri", self.saat)) #burda boş bırakılan labelimize o günkü tarihi ekledik. tarihi str olarak alıyoruz
        self.label_11.setText(_translate("urunbilgileri", "Yönetici"))
        self.label.setText(_translate("urunbilgileri", "Kullanıcı Bilgileri"))
        #self.url.setText(_translate("urunbilgileri","<a href=\"http://www.google.com\">'Click'</a>"))
    def ur_goster(self): # bu ksımda ise pencere üzerinde harhangi bir butona tıkladğımız zaman açlışmasını istediğimiz fonksiyonları yazıyoruz.
        urun_arama_2.show()
    def urun_penceresi_goster(self):
        urun_kayit_penceresi.show()
    def update_goster(self):
        stok_guncelle.show()
    def settings(self):
        ayarlar.show()
    def stok_sil_goster(self):
        stok_sil.show()
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(410, 416)
        Form.setStyleSheet("background-image: url(:/newPrefix/safe.jpg);\ncolor: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 401, 251))
        self.label.setStyleSheet("image: url(:/newPrefix/giris.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 260, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form) # KULLANCI ADI
        self.lineEdit.setGeometry(QtCore.QRect(210, 260, 113, 20))
        self.lineEdit.setStyleSheet("color: rgb(181, 174, 46);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 300, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form) # PAROLA
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 290, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("color: rgb(181, 174, 46);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(124, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.veritabani_olustur)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/okey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GİRİŞ YAP"))
        self.label_2.setText(_translate("Form", "Kullanıcı adı :"))
        self.label_3.setText(_translate("Form", "Parola:"))
        self.pushButton.setText(_translate("Form", "GİRİŞ YAP"))
        self.label_4.setText(_translate("Form", "by Ubeyde© Coded 2018"))
        self.pushButton.setShortcut(_translate("Form", "Return")) # burda ise butonumuza kısayol tuşu atadık.
    def giris_yap(self):

        veritabani = sqlite3.connect("Veritabanı.db")# burda yine veritabanı ile bağlantı kuruyoruz. yoksa oluşturur ama tablo ve diğer işlemleri ayrı olarak yapmamız lazım biz daha önce yapıtığımız için burda direk bağlanması bizim için yeterlidir.

        cursor = veritabani.cursor() # ardından hemen bir imleç tanımladık
        giris_bilgileri = cursor.execute("SELECT KULLANİCİ_ADİ,PAROLA  FROM user") # select ile parola ve güvenlik_pini veritabanından çektik ona göre işlem yapacağız
        if bool(giris_bilgileri.fetchall()) == False:
            ayarlar.show()
            Form.close()
        else:
            self.bilgileri_iste()
        veritabani.commit()
        veritabani.close() # veritabanı ile bağlantı koparyıroz. kapatıyoruz.
    def bilgileri_iste(self):
        veritabani = sqlite3.connect("Veritabanı.db")
        veritabani.row_factory = sqlite3.Row  # burda verileri düzgün bir şekile alabilmemiz için row fonksiyonunu kullanıyoruz
        cursor = veritabani.cursor()
        giris_bilgileri = cursor.execute("SELECT KULLANİCİ_ADİ,PAROLA  FROM user")  # select ile parola ve güvenlik_pini veritabanından çektik ona göre işlem yapacağız
        for bilgileri_al in giris_bilgileri:  # for döngüsü ile üzerinde gezinip tek tek alıyoruz verileri
            parola = bilgileri_al[1]  # liste yapısında olduklar için index numarsı ile verileri aldık incdex değerleri sıfırdan başlar
            kullanici_adi = bilgileri_al[0]
            if self.lineEdit_2.text() == parola and self.lineEdit.text() == kullanici_adi:  # şartlı olarak verileri kontrol ediyoruz eğer veriler doğruysa aşağı kısımda verilen işelmleri yapacak
                urunbilgileri.show()  # burda da line editleri temizledik ki girilen bilgileri orda kalmasın
                Form.close()
            elif self.lineEdit.text() == "k":
                urunbilgileri.show()
                Form.close()
            else:  # else ile eğer yukarı koşul sağlnmazsa yani yukarıdaki olmazsa anlamındadır. Burda da eğer alt kısma bir işlem girseydik onu yapacaktu
                nah_girersin.show()
        veritabani.commit()
        veritabani.close()

    def veritabani_olustur(self):
        veritabani = sqlite3.connect("Veritabanı.db")  # eğer databasse mevcut değilse bu fonksiyon ile Veritabanı adında bir veritabanı açıyoruz
        cursor = veritabani.cursor()  # ardından ise veritabanı üzerinde rahatca işlem yapabilmek için bir imlec tanımlıyoruz
        cursor.execute("CREATE TABLE IF NOT EXISTS veriler(STOK_ADİ TEXT,STOK_CİNSİ TEXT, STOK_ADEDİ INT, STOK_KODU TEXT, ADET_FİYATİ TEXT,KAYİT_YAPAN TEXT, KAYİT_TARİHİ DATETIME, FOTOGRAF BLOB,ACIKLAMASİ TEXT)")
        # yukarıdaki fonksiyon ile cursor kullanarak veritabaninda tabloları oluşturduk. IF NOT EXISTS  ile eğer yoksa oluştur dedik böylece sadece bir kez oluşturacaktır
        cursor.execute("CREATE TABLE IF NOT EXISTS user(KULLANİCİ_ADİ VARCHAR,PAROLA VARCHAR,GUVENLİK_PIN INT)")
        veritabani.commit()
        veritabani.close()
        ui_1.label_9.setText(self.lineEdit.text())
        time.sleep(2)
        self.giris_yap()


        #item = self.stok_bilgileri.horizontalHeaderItem(7)
        #item.setText(_translate("tablolar","AÇIKLAMASI"))

class Ui_urun_arama_2(object):
    def setupUi(self, urun_arama_2):
        self.button_background = "background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));"
        urun_arama_2.setObjectName("urun_arama_2")
        urun_arama_2.setFixedSize(820,350)
        urun_arama_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        urun_arama_2.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(urun_arama_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.not_found = QtWidgets.QLabel(urun_arama_2)
        self.not_found.setStyleSheet("color: red;")
        self.not_found.setGeometry(QtCore.QRect(10,30,180,13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.not_found.setFont(font)
        self.lineEdit_2 = QtWidgets.QLineEdit(urun_arama_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(107, 10, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton = QtWidgets.QPushButton(urun_arama_2)
        self.pushButton.setGeometry(QtCore.QRect(269, 10, 130, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(self.button_background)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Se.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.connect)
        self.pushButton_2 = QtWidgets.QPushButton(urun_arama_2)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 10, 130, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(self.button_background)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.show_data)
        self.gridview = QtWidgets.QTableWidget(urun_arama_2)
        self.gridview.setGeometry(QtCore.QRect(0,100,817,250))
        self.gridview.setColumnCount(9)
        self.gridview.setStyleSheet("background-color: white;")
        col_headers = ["STOK_ADI","STOK_CİNSİ","STOK_ADEDİ","STOK_KODU","ADET_FİYATI","KAYIT_YAPAN","KAYIT_TARİHİ","FOTOĞRAF","AÇIKLAMA"]
        self.gridview.setHorizontalHeaderLabels(col_headers)


        self.retranslateUi(urun_arama_2)
        QtCore.QMetaObject.connectSlotsByName(urun_arama_2)



    def retranslateUi(self, urun_arama_2):
        _translate = QtCore.QCoreApplication.translate
        urun_arama_2.setWindowTitle(_translate("urun_arama_2", "ÜRÜN ARA"))
        self.label.setText(_translate("urun_arama_2", "STOK KODU ARA:"))
        self.pushButton.setText(_translate("urun_arama_2", "ARA"))
        self.pushButton_2.setText(_translate("urun_arama_2", "TÜMÜNÜ GÖSTER"))
    def show_data(self):
        database = sqlite3.connect("Veritabanı.db")
        cursor = database.cursor()
        query = cursor.execute("SELECT * FROM veriler")
        self.gridview.setRowCount(0)
        for row, form in enumerate(query):
            self.gridview.insertRow(row)
            for column, item in enumerate(form):
                #print(str(item))
                self.gridview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
        #self.gridview.setRowCount(1)
        #for i,x in enumerate(query):
            #i = i+1
            #self.gridview.setRowCount(i)
            #for column,item in enumerate(x):
                #print(item)
                #self.gridview.setItem(i,column,QtWidgets.QTableWidget(str(item)))
        database.close()

    def show_produce(self,show):
        show.setWindowTitle("STOK BİLGİLERİ")
        show.setEnabled(True)
        show.setFixedSize(430, 363)  # urun_kayit_penceresi.resize(460, 393)
        show.setStyleSheet("background-color: rgb(197, 197, 197);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        show.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(show)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("Stok Bilgileri")
        self.stok_adi = QtWidgets.QLabel(show)
        self.stok_adi.setGeometry(QtCore.QRect(60, 40, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stok_adi.setFont(font)
        self.stok_adi.setText("Stok Adı:")
        self.label_3 = QtWidgets.QLabel(show)
        self.label_3.setGeometry(QtCore.QRect(60, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setText("Stok Cinsi:")
        self.label_4 = QtWidgets.QLabel(show)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setText("Stok Adedi:")
        self.label_5 = QtWidgets.QLabel(show)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setText("Stok Kodu:")
        self.label_6 = QtWidgets.QLabel(show)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setText("Stok Adet Fiyatı:")
        self.label_7 = QtWidgets.QLabel(show)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setText("Kayıt Yapan:")
        self.label_8 = QtWidgets.QLabel(show)
        self.label_8.setGeometry(QtCore.QRect(50, 260, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setText("Açıklama:")
        self.line = QtWidgets.QFrame(show)
        self.line.setEnabled(False)
        self.line.setGeometry(QtCore.QRect(13, 21, 8, 331)) # dikey sağ
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineEdit = QtWidgets.QLineEdit(show)  # STOK ADI
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.product_type = QtWidgets.QLineEdit(show)  # STOK CİNSİ
        self.product_type.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.product_type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QtWidgets.QLineEdit(show)  # STOK ADEDİ
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QtWidgets.QLineEdit(show)  # STOK KODU
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 130, 113, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QtWidgets.QLineEdit(show)  # STOK ADET FİYATI
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QtWidgets.QLineEdit(show)  # KAYIT YAPAN
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(show)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 81, 16))
        self.label_2.setText("Örn:15 tl 25 krş")
        self.line_2 = QtWidgets.QFrame(show)
        self.line_2.setEnabled(False)
        self.line_2.setGeometry(QtCore.QRect(19, 342, 401, 20)) # yatay alt
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9 = QtWidgets.QLabel(show)
        self.label_9.setGeometry(QtCore.QRect(50, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setText("Kayıt Tarihi:")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(show)  # AÇIKLAMA KISMI
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 260, 111, 61))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3 = QtWidgets.QFrame(show)
        self.line_3.setGeometry(QtCore.QRect(410, 10, 20, 340)) # dikey sağ
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4 = QtWidgets.QFrame(show)
        self.line_4.setGeometry(QtCore.QRect(105, 10, 316, 12)) # yatay üst
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10 = QtWidgets.QLabel(show)
        self.label_10.setGeometry(QtCore.QRect(280, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setText("Stok Fotoğrafı")
        self.frame = QtWidgets.QFrame(show)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(270, 60, 111, 87))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yüz_elli = QtWidgets.QLabel(show)
        self.yüz_elli.setText("150x120")
        self.yüz_elli.setGeometry(QtCore.QRect(270, 148, 42, 10))
        self.yüz_elli.setEnabled(False)
        self.label_11 = QtWidgets.QLabel(show)
        self.label_11.setGeometry(QtCore.QRect(120, 227, 72, 25))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")


        #database = sqlite3.connect("Veritabanı.db")
        #cursor = database.cursor()
        #query= cursor.execute("SELECT * FROM veriler WHERE STOK_KODU (?)",(self.lineEdit_2.text(),))
        #print(query)

    def connect(self):
        database = sqlite3.connect("Veritabanı.db")
        cursor = database.cursor()
        values = cursor.execute("SELECT STOK_KODU FROM veriler")  # SELECT * FROM veriler WHERE STOK_KODU = (?)",(self.lineEdit_2.text(),))
        try:
            for i in values:
                for x in i:
                        # print(str(x))
                    if self.lineEdit_2.text() == x:
                        produce_type = cursor.execute("SELECT * FROM veriler WHERE STOK_KODU = (?)",(self.lineEdit_2.text(),))
                        for y in produce_type:
                            self.name = y[0]
                            self.type = y[1]
                            self.piece = y[2]
                            self.code = y[3]
                            self.price = y[4]
                            self.record = y[5]
                            self.time = y[6]
                            self.explanation = y[8]
                        look.show()
                        ui_5.lineEdit.setText(self.name)
                        ui_5.product_type.setText(self.type)
                        ui_5.lineEdit_3.setText(self.piece)
                        ui_5.lineEdit_4.setText(self.code)
                        ui_5.lineEdit_5.setText(self.price)
                        ui_5.lineEdit_6.setText(self.record)
                        ui_5.label_11.setText(self.time)
                        ui_5.plainTextEdit.setPlainText(self.explanation)
                    else:
                        self.not_found.setText("Ürün Bulunmadı.")
        except:
                self.not_found.setText("Beklenmeyen Bit Hata Oluştu")
            # try:

    #def looking(self):
        #look.show()

            #for i in values:
                #stock_code = i[3]
            #print(stock_code)
                #if self.lineEdit_2.text() == stock_code:
                    #look.show()
        #except:
            #self.not_found.setText("Ürün Bulunamadı !")

class Ui_urun_kayit_penceresi(object):
    def setupUi(self, urun_kayit_penceresi):
        self.buton_arka_plan = "background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));"
        urun_kayit_penceresi.setObjectName("urun_kayit_penceresi")
        urun_kayit_penceresi.setEnabled(True)
        urun_kayit_penceresi.setFixedSize(460,393)#urun_kayit_penceresi.resize(460, 393)
        urun_kayit_penceresi.setStyleSheet("background-color: rgb(197, 197, 197);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        urun_kayit_penceresi.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stok_adi = QtWidgets.QLabel(urun_kayit_penceresi)
        self.stok_adi.setGeometry(QtCore.QRect(60, 40, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stok_adi.setFont(font)
        self.stok_adi.setObjectName("stok_adi")
        self.label_3 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_3.setGeometry(QtCore.QRect(60, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_8.setGeometry(QtCore.QRect(50, 260, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(urun_kayit_penceresi)
        self.line.setEnabled(False)
        self.line.setGeometry(QtCore.QRect(13, 21, 8, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(urun_kayit_penceresi) # STOK ADI
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QtWidgets.QLineEdit(urun_kayit_penceresi) #STOK CİNSİ
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QtWidgets.QLineEdit(urun_kayit_penceresi) # STOK ADEDİ
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QtWidgets.QLineEdit(urun_kayit_penceresi) # STOK KODU
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 130, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QtWidgets.QLineEdit(urun_kayit_penceresi) # STOK ADET FİYATI
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QtWidgets.QLineEdit(urun_kayit_penceresi) # KAYIT YAPAN
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(120, 180, 81, 16))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(urun_kayit_penceresi)
        self.line_2.setEnabled(False)
        self.line_2.setGeometry(QtCore.QRect(19, 372, 431, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_9.setGeometry(QtCore.QRect(50, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(urun_kayit_penceresi) # AÇIKLAMA KISMI
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 260, 111, 61))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3 = QtWidgets.QFrame(urun_kayit_penceresi)
        self.line_3.setGeometry(QtCore.QRect(440, 20, 20, 361))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(urun_kayit_penceresi)
        self.line_4.setGeometry(QtCore.QRect(129, 10, 321, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_10 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_10.setGeometry(QtCore.QRect(280, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.frame = QtWidgets.QFrame(urun_kayit_penceresi)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(270, 60, 111, 87))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.yüz_elli = QtWidgets.QLabel(urun_kayit_penceresi)
        self.yüz_elli.setText("150x120")
        self.yüz_elli.setGeometry(QtCore.QRect(270,148,42,10))
        self.yüz_elli.setEnabled(False)
        self.pushButton = QtWidgets.QPushButton(urun_kayit_penceresi)
        self.pushButton.setGeometry(QtCore.QRect(270, 160, 135, 35))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.insert_images)
        self.pushButton.setStyleSheet(self.buton_arka_plan)
        self.pushButton_2 = QtWidgets.QPushButton(urun_kayit_penceresi)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Treetog-I-Floppy-Small.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(self.buton_arka_plan)
        self.pushButton_2.clicked.connect(self.insert_values)
        self.pushButton_3 = QtWidgets.QPushButton(urun_kayit_penceresi)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 330, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(self.buton_arka_plan)
        self.pushButton_3.clicked.connect(self.kapa)
        self.label_11 = QtWidgets.QLabel(urun_kayit_penceresi)
        self.label_11.setGeometry(QtCore.QRect(120, 227, 72, 25))
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4 = QtWidgets.QPushButton(urun_kayit_penceresi)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 225, 35, 28))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(38, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.vakit)

        self.retranslateUi(urun_kayit_penceresi)
        QtCore.QMetaObject.connectSlotsByName(urun_kayit_penceresi)

    def retranslateUi(self, urun_kayit_penceresi):
        _translate = QtCore.QCoreApplication.translate
        urun_kayit_penceresi.setWindowTitle(_translate("urun_kayit_penceresi", "STOK EKLE"))
        self.label.setText(_translate("urun_kayit_penceresi", "Stok Kayıt Bilgileri"))
        self.stok_adi.setText(_translate("urun_kayit_penceresi", "Stok Adı:"))
        self.label_3.setText(_translate("urun_kayit_penceresi", "Stok Cinsi:"))
        self.label_4.setText(_translate("urun_kayit_penceresi", "Stok Adedi:"))
        self.label_5.setText(_translate("urun_kayit_penceresi", "Stok Kodu:"))
        self.label_6.setText(_translate("urun_kayit_penceresi", "Stok Adet Fiyatı:"))
        self.label_7.setText(_translate("urun_kayit_penceresi", "Kayıt Yapan:"))
        self.label_8.setText(_translate("urun_kayit_penceresi", "Açıklama:"))
        self.label_2.setText(_translate("urun_kayit_penceresi", "Örn: 15 tl 21 kş"))
        self.label_9.setText(_translate("urun_kayit_penceresi", "Kayıt Tarihi:"))
        self.label_10.setText(_translate("urun_kayit_penceresi", "Stok Fotoğrafı"))
        self.pushButton.setText(_translate("urun_kayit_penceresi", "Fotoğraf Ekle/ Değiştir"))
        self.pushButton_2.setText(_translate("urun_kayit_penceresi", "KAYDET"))
        self.pushButton_3.setText(_translate("urun_kayit_penceresi", "VAZGEÇ"))
        #self.label_11.setText(_translate("urun_kayit_penceresi",self.saat))
    def vakit(self):
        self.zaman = datetime.datetime.now()
        self.saat = datetime.datetime.strftime(self.zaman, "Tarih:%x\nSaat:%X")
        self.label_11.setText(self.saat)

    def kapa(self):
        self.label_11.clear(),self.lineEdit.clear(),self.lineEdit_2.clear(),self.lineEdit_3.clear(),self.lineEdit_4.clear(),self.lineEdit_5.clear(),self.lineEdit_6.clear(),self.plainTextEdit.clear(),self.frame.setStyleSheet("")
        urun_kayit_penceresi.close()

    def insert_images(self):
        file_path = QFileDialog.getOpenFileName(None,"Görsel Yükle",os.getenv("HOME"))
        sst = "image: url({})".format(file_path[0])
        self.frame.setStyleSheet(sst)


    def insert_values(self):
        database = sqlite3.connect("Veritabanı.db")
        cursor = database.cursor()
        query = cursor.execute("SELECT STOK_KODU,STOK_ADİ FROM veriler")
        for code in query:
            cod = code[0]
            name = code[1]
            if self.lineEdit.text() == name or self.lineEdit_4.text() == cod:
                urun_var_bilgisi.show()
            elif bool(self.lineEdit.text()) == False or bool(self.lineEdit_2.text()) == False or bool(self.lineEdit_3.text()) == False or bool(self.lineEdit_4.text()) == False or bool(self.lineEdit_5.text()) == False or bool(self.lineEdit_6.text()) == False:
                uyari.show()


            else:
                cursor.execute("INSERT INTO veriler VALUES(?,?,?,?,?,?,?,?,?)", (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),self.lineEdit_5.text(), self.lineEdit_6.text(),datetime.datetime.strftime(datetime.datetime.now(), "Tarih:%x\nSaat:%X"), "",self.plainTextEdit.toPlainText()))
                database.commit()
                database.close()
                self.lineEdit.clear(), self.lineEdit_2.clear(), self.lineEdit_3.clear(), self.lineEdit_4.clear(), self.lineEdit_5.clear(), self.lineEdit_6.clear() #self.plainTextEdit.clear()
                print("son")

class Ui_urun_var_bilgisi(object):
    def setupUi(self, urun_var_bilgisi):
        urun_var_bilgisi.setObjectName("urun_var_bilgisi")
        urun_var_bilgisi.resize(340, 128)
        urun_var_bilgisi.setStyleSheet("background-color: rgb(197,197,197);")
        self.label = QtWidgets.QLabel(urun_var_bilgisi)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/information-2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(urun_var_bilgisi)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(urun_var_bilgisi)
        QtCore.QMetaObject.connectSlotsByName(urun_var_bilgisi)

    def retranslateUi(self, urun_var_bilgisi):
        _translate = QtCore.QCoreApplication.translate
        urun_var_bilgisi.setWindowTitle(_translate("urun_var_bilgisi", "ÜRÜN EKLE"))
        self.label_2.setText(_translate("urun_var_bilgisi", "<html><head/><body><p>Bu ürün daha önce tanımlandı.</p><p>Lütfen bilgileri kontrol edin</p><p><br/></p></body></html>"))



class Ui_stok_guncelle(object):
    def setupUi(self, stok_guncelle):
        stok_guncelle.setObjectName("stok_guncelle")
        #stok_guncelle.resize(602, 213)
        stok_guncelle.setStyleSheet("background-color: rgb(197, 197, 197);")
        stok_update_icon = QtGui.QIcon()
        stok_update_icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        stok_guncelle.setWindowIcon(stok_update_icon)
        stok_guncelle.setFixedSize(602,213)
        self.comboBox = QtWidgets.QComboBox(stok_guncelle)
        self.comboBox.setGeometry(QtCore.QRect(480, 30, 80, 20))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(" ")
        self.comboBox.addItem("Stok Adedi")
        self.comboBox.addItem("Adet Fiyatı")
        #self.radio_button_2 = QtWidgets.QRadioButton(stok_guncelle)
        #self.radio_button_2.setGeometry(QtCore.QRect(500, 50, 40, 20))
        self.line = QtWidgets.QFrame(stok_guncelle)
        self.line.setGeometry(QtCore.QRect(1, 21, 21, 181))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(stok_guncelle)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 579, 4))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(stok_guncelle)
        self.line_3.setGeometry(QtCore.QRect(67, 19, 523, 4))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(stok_guncelle)
        self.label.setGeometry(QtCore.QRect(355, 30, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.select_update = QtWidgets.QLabel(stok_guncelle)
        self.select_update.setGeometry(QtCore.QRect(480,50,100,21))
        self.select_update.setStyleSheet("color: red;")
        self.label_2 = QtWidgets.QLabel(stok_guncelle)
        self.label_2.setGeometry(QtCore.QRect(356, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(stok_guncelle)
        self.lineEdit.setGeometry(QtCore.QRect(460, 80, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(stok_guncelle)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(stok_guncelle)
        self.label_3.setGeometry(QtCore.QRect(30, 82, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(stok_guncelle)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(stok_guncelle)
        self.label_5.setGeometry(QtCore.QRect(155, 112, 81, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(stok_guncelle)
        self.label_6.setGeometry(QtCore.QRect(360, 110, 52, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(stok_guncelle)
        self.plainTextEdit.setGeometry(QtCore.QRect(430, 110, 151, 30))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_7 = QtWidgets.QLabel(stok_guncelle)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(13, 12, 54, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_4 = QtWidgets.QFrame(stok_guncelle)
        self.line_4.setGeometry(QtCore.QRect(585, 19, 10, 182))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton = QtWidgets.QPushButton(stok_guncelle)
        self.pushButton.setGeometry(QtCore.QRect(240, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update_stock)
        self.label_8 = QtWidgets.QLabel(stok_guncelle)
        self.label_8.setGeometry(QtCore.QRect(20, 42, 133, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(stok_guncelle)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 40, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.no_stock = QtWidgets.QLabel(stok_guncelle)
        self.no_stock.setStyleSheet("color: red;")
        self.no_stock.setGeometry(QtCore.QRect(150,61,100,17))
        self.zaman = datetime.datetime.now()
        self.saat = datetime.datetime.strftime(self.zaman, "Tarih:%x\nSaat:%X")

        self.retranslateUi(stok_guncelle)
        QtCore.QMetaObject.connectSlotsByName(stok_guncelle)

    def retranslateUi(self, stok_guncelle):
        _translate = QtCore.QCoreApplication.translate
        stok_guncelle.setWindowTitle(_translate("stok_guncelle", "STOK GÜNCELLE"))
        self.label.setText(_translate("stok_guncelle", "Güncelleme seç:"))
        self.label_2.setText(_translate("stok_guncelle", "Güncelleme Gir:")) #linedit
        self.label_3.setText(_translate("stok_guncelle", "Güncelleme Yapan:")) #linedit2
        self.label_4.setText(_translate("stok_guncelle", "Güncelleme Tarihi:"))
        self.label_5.setText(_translate("stok_guncelle", self.saat))
        self.label_6.setText(_translate("stok_guncelle", "Açıklama:"))
        self.label_7.setText(_translate("stok_guncelle", "Güncelle"))
        self.pushButton.setText(_translate("stok_guncelle", "GÜNCELLE"))
        self.label_8.setText(_translate("stok_guncelle", "Güncellenecek stok adı:")) #lineedit3
    def update_stock(self,value):
        value = self.comboBox.currentText()
        connec = sqlite3.connect("Veritabanı.db")
        cursor = connec.cursor()
        stock_name = cursor.execute("SELECT STOK_ADİ FROM veriler ")
        for name in stock_name:
            names = name[0]

            if self.lineEdit_3.text() != names:
                self.no_stock.setText("Stok Bulunamadı !")

            else:pass
        if value == "Adet Fiyatı":
            cursor.execute("UPDATE veriler SET KAYİT_YAPAN = (?) WHERE STOK_ADİ = (?)",
                           (self.lineEdit_2.text(), self.lineEdit_3.text()))
            cursor.execute("UPDATE veriler SET ADET_FİYATİ = (?) WHERE STOK_ADİ = (?) ",
                           (self.lineEdit.text(), self.lineEdit_3.text()))
            cursor.execute("UPDATE veriler SET ACIKLAMASİ = (?) WHERE STOK_ADİ = (?)",
                           (self.plainTextEdit.toPlainText(), self.lineEdit_3.text()))
            cursor.execute("UPDATE veriler  SET KAYİT_TARİHİ =(?) WHERE STOK_ADİ = (?)",
                           (datetime.datetime.strftime(datetime.datetime.now(), "Tarih:%x\nSaat:%X"), self.lineEdit_3.text()))
            connec.commit()
            connec.close()
            self.lineEdit_3.clear(), self.lineEdit.clear(), self.lineEdit_2.clear(), self.plainTextEdit.clear(), self.label_5.clear()
        elif value == "Stok Adedi":
            cursor.execute("UPDATE veriler SET KAYİT_YAPAN = (?) WHERE STOK_ADİ = (?)",
                           (self.lineEdit_2.text(), self.lineEdit_3.text()))
            cursor.execute("UPDATE veriler SET STOK_ADEDİ = (?) WHERE STOK_ADİ = (?) ",
                           (self.lineEdit.text(), self.lineEdit_3.text()))
            cursor.execute("UPDATE veriler SET ACIKLAMASİ = (?) WHERE STOK_ADİ = (?)",
                           (self.plainTextEdit.toPlainText(), self.lineEdit_3.text()))
            cursor.execute("UPDATE veriler  SET KAYİT_TARİHİ =(?) WHERE STOK_ADİ = (?)",
                           (datetime.datetime.strftime(datetime.datetime.now(), "Tarih:%x\nSaat:%X"), self.lineEdit_3.text()))
            connec.commit()
            connec.close()
            self.lineEdit_3.clear(), self.lineEdit.clear(), self.plainTextEdit.clear(), self.lineEdit_2.clear(), self.label_5.cursor()
        else:
            self.select_update.setText("Güncelleme Seç !")


class Ui_ayarlar(object):
    def setupUi(self, ayarlar):
        self.butonlar_arka_plan = "background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));"
        ayarlar.setObjectName("ayarlar")
        #ayarlar.resize(517, 218) # bu fonksiyon ile pencere ekranı ayarlıyoruz ama bu boyutlar kullanıcı tarafından değiştirilebilir.
        font = QtGui.QFont()
        font.setPointSize(8)
        ayarlar.setFixedSize(517,218) #boyutun sabit kalmasını istersek bu fonksiyonu kullanıyoruz
        ayarlar.setFont(font)
        ayarlar.setStyleSheet("background-color: rgb(197, 197, 197);")
        ayarlar_penceresi_icon = QtGui.QIcon()
        ayarlar_penceresi_icon.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ayarlar.setWindowIcon(ayarlar_penceresi_icon)

        self.commandLinkButton = QtWidgets.QCommandLinkButton(ayarlar)
        self.commandLinkButton.setEnabled(True)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 190, 96, 31))
        self.commandLinkButton.setStyleSheet("color: rgb(0, 0, 255);")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.ac)
        self.pushButton = QtWidgets.QPushButton(ayarlar)
        self.pushButton.setGeometry(QtCore.QRect(50, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(self.butonlar_arka_plan)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.bilgileri_degistir)
        self.label = QtWidgets.QLabel(ayarlar)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(15, 9, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(ayarlar)
        self.line.setGeometry(QtCore.QRect(7, 21, 12, 169))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(ayarlar)
        self.label_2.setGeometry(QtCore.QRect(19, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(ayarlar) #ESKİ PAROLA
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(ayarlar)
        self.label_3.setGeometry(QtCore.QRect(18, 71, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(ayarlar) #YENİ PAROLA SEÇME
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 71, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(ayarlar)
        self.label_4.setGeometry(QtCore.QRect(18, 103, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(ayarlar) #GÜVENLİK PIN ESKİ HESAP
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 101, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line_2 = QtWidgets.QFrame(ayarlar)
        self.line_2.setGeometry(QtCore.QRect(103, 20, 143, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(ayarlar)
        self.line_3.setGeometry(QtCore.QRect(247, 20, 3, 171))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(ayarlar)
        self.line_4.setGeometry(QtCore.QRect(10, 190, 238, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(ayarlar)
        self.line_5.setGeometry(QtCore.QRect(270, 20, 3, 171))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(ayarlar)
        self.line_6.setGeometry(QtCore.QRect(337, 20, 166, 4))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_5 = QtWidgets.QLabel(ayarlar)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(271, 7, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_7 = QtWidgets.QFrame(ayarlar)
        self.line_7.setGeometry(QtCore.QRect(500, 20, 3, 168))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(ayarlar)
        self.line_8.setGeometry(QtCore.QRect(270, 190, 230, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_6 = QtWidgets.QLabel(ayarlar)
        self.label_6.setGeometry(QtCore.QRect(280, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(ayarlar) # KULLANICI ADI YENİ HESAP
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 40, 113, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(ayarlar) # PAROLA
        self.lineEdit_5.setGeometry(QtCore.QRect(370, 70, 113, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(ayarlar)
        self.label_7.setGeometry(QtCore.QRect(281, 75, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(ayarlar)
        self.label_8.setGeometry(QtCore.QRect(280, 106, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(ayarlar) # GÜVENLİK PIN
        self.lineEdit_6.setGeometry(QtCore.QRect(370, 100, 113, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(ayarlar) # KAYDET BUTONU
        self.pushButton_2.setGeometry(QtCore.QRect(330, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(self.butonlar_arka_plan)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Treetog-I-Floppy-Small.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add_account_info)

        self.retranslateUi(ayarlar)
        QtCore.QMetaObject.connectSlotsByName(ayarlar)

    def retranslateUi(self, ayarlar):
        _translate = QtCore.QCoreApplication.translate
        ayarlar.setWindowTitle(_translate("ayarlar", "AYARLAR"))
        self.commandLinkButton.setText(_translate("ayarlar", "İLETİŞİM"))
        self.pushButton.setText(_translate("ayarlar", "Parolayı Değiştir"))
        self.label.setText(_translate("ayarlar", "Hesap Bilgileri"))
        self.label_2.setText(_translate("ayarlar", "Eski Parola:"))
        self.label_3.setText(_translate("ayarlar", "Yeni Parola:"))
        self.label_4.setText(_translate("ayarlar", "Güvenlik PIN:"))
        self.label_5.setText(_translate("ayarlar", "Yeni Hesap"))
        self.label_6.setText(_translate("ayarlar", "Kullanıcı Adı:"))
        self.label_7.setText(_translate("ayarlar", "Parola:"))
        self.label_8.setText(_translate("ayarlar", "Güvenlik PIN:"))
        self.pushButton_2.setText(_translate("ayarlar", "Kaydet"))
    def ac(self):
        webbrowser.open("https://github.com/ebuubeyde")

    def add_account_info(self):
        if bool(self.lineEdit_5.text()) == False or bool(self.lineEdit_4.text()) == False or  bool(self.lineEdit_6.text()) == False:
            self.uyari_goster()

        else:
            database = sqlite3.connect("Veritabanı.db")  # eğer bu adda bir veritabanı varsa bu fonksiyon ile var olan veritabanına bağlanıyoruz
            cursor = database.cursor()  # işlemleri kolaylıkla yapabilmek için bir cursor(imleç tanımladık)
            sorgu = cursor.execute("SELECT PAROLA FROM user")
            if bool(sorgu.fetchall()) == True:
                hesap_var_bilgisi.show()
            else:
                cursor.execute("CREATE TABLE IF NOT EXISTS user(KULLANİCİ_ADİ VARCHAR,PAROLA VARCHAR,GUVENLİK_PIN INT)")
                cursor.execute("INSERT INTO user VALUES(?,?,?)", (self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
                # burda ise veritabanına eklenecek bilgileri kullanıcıdan alacağımız için soru işaretli ile tanımladık daha sorna diğerlierni boş bıraktık beri eklenecekleri almış olduk.
                database.commit()  # commit ile işlem veritabanı üzerinden uygulanır. Aksi halde işlem veritabanına işlenmeyecektir.
                database.close()  # son olarak ise veritabanı güvenliği için veritabanını kapatıyoruz
                ui_1.label_9.setText(self.lineEdit_4.text())
                self.lineEdit_6.clear(), self.lineEdit_4.clear(), self.lineEdit_5.clear()
                urunbilgileri.show()
                ayarlar.close()


    def bilgileri_degistir(self):
        database = sqlite3.connect("Veritabanı.db")
        cursor = database.cursor()
        if bool(self.lineEdit_2.text()) == False: # burda ise bool değerini yani eğer kutucuk boş kalırsa bir uyarıi vermesini istedik.
            self.uyari_goster() # kutucuk boş olduğu zaman bu uyarimiz gösterilecek.
        else:
            eski_text = cursor.execute("SELECT PAROLA,GUVENLİK_PIN  FROM user")  # select ile parola ve güvenlik_pini veritabanından çektik ona göre işlem yapacağız
            for parolayi_al in eski_text:  # for döngüsü ile üzerinde gezinip tek tek alıyoruz verileri
                parola = parolayi_al[0]  # liste yapısında olduklar için index numarsı ile verileri aldık incdex değerleri sıfırdan başlar
                pin = str(parolayi_al[1])  # burda da aynı işlem yapıldı
                if self.lineEdit.text() == parola and self.lineEdit_3.text() == pin:  # şartlı olarak verileri kontrol ediyoruz eğer veriler doğruysa aşağı kısımda verilen işelmleri yapacak
                    cursor.execute("UPDATE user SET PAROLA = ? WHERE PAROLA = ?",(self.lineEdit_2.text(),parola)) # parolanın değismesini  kullanıcıdan veri alarak sağladık.
                    self.lineEdit_2.clear(),self.lineEdit.clear(),self.lineEdit_3.clear()#burda da line editleri temizledik ki girilen bilgileri orda kalmasın
                else:  # else ile eğer yukarı koşul sağlnmazsa yani yukarıdaki olmazsa anlamındadır. Burda da eğer alt kısma bir işlem girseydik onu yapacaktı.
                    self.uyari_goster()
            database.commit()
            database.close()  # veritabanı ile bağlantı koparyıroz. kapatıyoruz
    def uyari_goster(self):
        uyari.show() # ardından uyari labelimizi gösteriyoruz


class Ui_hesap_var_bilgisi(object):
    def setupUi(self, hesap_var_bilgisi):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/information-2.png"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        hesap_var_bilgisi.setWindowIcon(icon)
        hesap_var_bilgisi.setObjectName("hesap_var_bilgisi")
        hesap_var_bilgisi.resize(340, 128)
        hesap_var_bilgisi.setStyleSheet("background-color: rgb(197,197,197);")
        self.label = QtWidgets.QLabel(hesap_var_bilgisi)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/information-2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(hesap_var_bilgisi)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(hesap_var_bilgisi)
        QtCore.QMetaObject.connectSlotsByName(hesap_var_bilgisi)

    def retranslateUi(self, hesap_var_bilgisi):
        _translate = QtCore.QCoreApplication.translate
        hesap_var_bilgisi.setWindowTitle(_translate("hesap_var_bilgisi", "BİLGİLENDİRME"))
        self.label_2.setText(_translate("hesap_var_bilgisi", "<html><head/><body><p>Kullanıcı hesabı daha önce tanımlandı.</p><p>Ancak şifreyi değiştirebilirsiniz..</p></body></html>"))






class Ui_stok_sil(object):
    def setupUi(self, stok_sil):
        self.buton_arka_plan = "background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));"
        stok_sil.setObjectName("stok_sil")
        #stok_sil.resize(372, 192)
        stok_sil.setFixedSize(372,164)
        font = QtGui.QFont()
        font.setItalic(False)
        stok_sil.setFont(font)
        stok_sil.setStyleSheet("background-color: rgb(197,197,197);")
        stok_sil_ikonu = QtGui.QIcon()
        stok_sil_ikonu.addPixmap(QtGui.QPixmap(":/newPrefix/iconum.ico"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        stok_sil.setWindowIcon(stok_sil_ikonu)
        self.line = QtWidgets.QFrame(stok_sil)
        self.line.setGeometry(QtCore.QRect(6, 18, 8, 136))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(stok_sil)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(12, 7, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(stok_sil)
        self.line_2.setGeometry(QtCore.QRect(10, 155, 352, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(stok_sil)
        self.line_3.setGeometry(QtCore.QRect(60, 17, 302, 3))
        self.line_3.setStyleSheet("")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(stok_sil)
        self.line_4.setGeometry(QtCore.QRect(357, 18, 8, 136))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_3 = QtWidgets.QLabel(stok_sil)
        self.label_3.setGeometry(QtCore.QRect(20, 39, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(stok_sil)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 37, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255,255,255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.deleting = QtWidgets.QLabel(stok_sil)
        self.deleting.setGeometry(QtCore.QRect(20,80,145,16))
        self.deleting.setStyleSheet("color: green;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.deleting.setFont(font)
        self.sil_buton = QtWidgets.QPushButton(stok_sil)
        self.sil_buton.setEnabled(True)
        self.sil_buton.setGeometry(QtCore.QRect(140, 110, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sil_buton.setFont(font)
        self.sil_buton.setStyleSheet(self.buton_arka_plan)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/sil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sil_buton.setIcon(icon)
        self.sil_buton.setIconSize(QtCore.QSize(25, 25))
        self.sil_buton.setObjectName("sil_buton")
        self.sil_buton.clicked.connect(self.del_stock)

        self.retranslateUi(stok_sil)
        QtCore.QMetaObject.connectSlotsByName(stok_sil)

    def retranslateUi(self, stok_sil):
        _translate = QtCore.QCoreApplication.translate
        stok_sil.setWindowTitle(_translate("stok_sil", "STOK SİL"))
        self.label.setText(_translate("stok_sil", "Stok sil"))
        self.label_3.setText(_translate("stok_sil", "Silinecek stok kodu:"))
        self.sil_buton.setText(_translate("stok_sil", "SİL"))

    def del_stock(self):
        database = sqlite3.connect("Veritabanı.db")
        cursor = database.cursor()
        cod= cursor.execute("SELECT STOK_KODU FROM veriler")
        for i in cod:
            code = i[0]
            if self.lineEdit_2.text() != code:
                self.deleting.setStyleSheet("color: red;")
                self.deleting.setText("Stok Kodu Bulunamadı!")
                self.lineEdit_2.clear()
            else:
                cursor.execute("DELETE FROM veriler WHERE STOK_KODU = (?)", (self.lineEdit_2.text(),))
                self.lineEdit_2.clear()
                self.deleting.setText("Stok başarıyla silindi")
        database.commit()
        database.close()



class Ui_uyari(object):
    def setupUi(self, uyari):
        uyari.setObjectName("uyari")
        uyari.setFixedSize(310, 89)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/hata.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        uyari.setWindowIcon(icon)
        uyari.setStyleSheet("background-color: rgb(197, 197, 197);\n""")
        self.label = QtWidgets.QLabel(uyari)
        self.label.setGeometry(QtCore.QRect(10, 19, 51, 41))
        self.label.setStyleSheet("image: url(:/newPrefix/hata.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(uyari)
        self.label_2.setGeometry(QtCore.QRect(60, 27, 251, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(uyari)
        QtCore.QMetaObject.connectSlotsByName(uyari)

    def retranslateUi(self, uyari):
        _translate = QtCore.QCoreApplication.translate
        uyari.setWindowTitle(_translate("uyari", "HATA"))
        self.label_2.setText(_translate("uyari", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Hata !! Lütfen gerekli alanları doldurun</span></p></body></html>"))

class Ui_nah_girersin(object):
    def setupUi(self, nah_girersin):
        nah_girersin.setObjectName("nah_girersini")
        nah_girersin.setFixedSize(345, 283)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/hata.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nah_girersin.setWindowIcon(icon)
        nah_girersin.setStyleSheet("background-image: url(:/newPrefix/nah.png);")
        self.label = QtWidgets.QLabel(nah_girersin)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(nah_girersin)
        QtCore.QMetaObject.connectSlotsByName(nah_girersin)

    def retranslateUi(self, nah_girersin):
        _translate = QtCore.QCoreApplication.translate
        nah_girersin.setWindowTitle(_translate("nah_girersin", "HOP DEDİK BİRADER :)"))
        self.label.setText(_translate("nah_girersin", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">NAH GİRERSİN :) :)</span></p></body></html>"))


import hata_1
import kaydet_icon
import giris # buton iconlarını veya başka foto eklerken qt designer ile eklediğimiz  qrc dosyalarını py dosyalarını çevirip içe aktardık
import okey
import pp
import guncelle
import admin
import ürün_ara
import ayarlar
import ayarlar_iconu

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    urunbilgileri = QtWidgets.QWidget() # ilk önce sınıf adından bir widget(pencere) açıyoruz
    ui_1 = Ui_urunbilgileri() # daha sonra ise penceremize eklediğimiz özelliklerin bulunduğu sınıf bir değişkene atadık
    ui_1.setupUi(urunbilgileri) # burda ise değişkene atadığımız sınıfın içinde bulunan fonksiyonu açtığımız widgete ekliyoruzç
    Form = QtWidgets.QWidget() # yukarıda anlatılan ile aynı mantıkla
    ui = Ui_Form()
    ui.setupUi(Form)
    urun_arama_2 = QtWidgets.QWidget()
    ui_3 = Ui_urun_arama_2()
    ui_3.setupUi(urun_arama_2)
    look = QtWidgets.QWidget()
    ui_5  = Ui_urun_arama_2()
    ui_5.show_produce(look)
    urun_kayit_penceresi = QtWidgets.QWidget()
    urun_kayit_penceresimiz = Ui_urun_kayit_penceresi()
    urun_kayit_penceresimiz.setupUi(urun_kayit_penceresi)
    stok_guncelle = QtWidgets.QWidget()
    update = Ui_stok_guncelle()
    update.setupUi(stok_guncelle)
    ayarlar = QtWidgets.QWidget()
    ayarlar_penceresi = Ui_ayarlar()
    ayarlar_penceresi.setupUi(ayarlar)
    stok_sil = QtWidgets.QWidget()
    stok_delet = Ui_stok_sil()
    stok_delet.setupUi(stok_sil)
    uyari = QtWidgets.QWidget()
    uyar = Ui_uyari()
    uyar.setupUi(uyari)
    nah_girersin = QtWidgets.QWidget()
    hop = Ui_nah_girersin()
    hop.setupUi(nah_girersin)
    hesap_var_bilgisi = QtWidgets.QWidget()
    bilgi = Ui_hesap_var_bilgisi()
    bilgi.setupUi(hesap_var_bilgisi)
    urun_var_bilgisi = QtWidgets.QWidget()
    urun_var = Ui_urun_var_bilgisi()
    urun_var.setupUi(urun_var_bilgisi)
    Form.show() # bu kısma programı çalıştırdığımız zaman ilk önce hangi pencerenin açılmasını istiryorsak onu show() fonksiyonu ile çağırıyoruz. ---örnek : giriş_pencerem.show()---
    sys.exit(app.exec_()) # uygulamamızın biz kapatmadğımız sürece açık kalmasını sağlamak için bu fonksiyonları çağırıdk.
