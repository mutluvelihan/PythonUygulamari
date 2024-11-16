isim=str(input("Lutfen Adinizi Giriniz: "))
Yas=int(input("Lutfen Yasinizi Giriniz: "))
Egitim=str(input("Lutfen Egitim Durumunuzu Giriniz (Turkce Karakter Kullanmayiz. Ornegin: Ilkokul-Ortaokul-Lise-Universite): "))
Egitim2=("Ilkokul","Ortaokul","Lise","Universite")

if Egitim not in Egitim2:
    print("Lutfen Gecerli Bir Egitim Durumu Giriniz!!!")
elif (Yas>=18) and (Egitim=="Lise" or Egitim=="Universite"):
    print("Ehliyet Sartlari Gecildi!!!")
else:
    print("Ehliyet Sartlari Gerceklesmiyor!!!")