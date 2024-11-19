Sayac=2

for i in range(0,30):

    Kullanici_Adi=input("Kullanici Adi: ")
    Kullanici_Sif=input("Sifre: ")
    SistemKA="Anlasilir Ekonomi"
    SistemSif="123456"

    if Kullanici_Adi==SistemKA and Kullanici_Sif==SistemSif:
        print("Giris Basarili, Hosgeldiniz!")
        break
    elif (Kullanici_Adi!=SistemKA or Kullanici_Sif!=SistemSif) and Sayac!=0:
        print("Hatali Giris Lutfen Tekrar Deneyiniz! Kalan Hakkiniz {}".format(Sayac))
        Sayac=Sayac-1
    else:
        print("Kalan Kullanim Hakkiniz {} Kapatiliyor...".format(Sayac))
        break