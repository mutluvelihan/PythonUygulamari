Kullanici_Adi=input("Lutfen Kullanici Adini Giriniz: ")
Kullanici_Sifre=input("Lutfen Sifrenizi Giriniz: ")

SistemKA="Velihan Mutlu"
SistemSif="123456"

if Kullanici_Adi==SistemKA and Kullanici_Sifre==SistemSif:
    print("Merhaba {}, Hosgeldin!!!".format(SistemKA))
elif Kullanici_Adi!=SistemKA and Kullanici_Sifre!=SistemSif:
    print("Merhaba, Kullanici Adi ve Sifresi Hatali!!!")
elif Kullanici_Adi!=SistemKA:
    print("Merhaba, Kullanici Adini Hatali Girdiniz!!!")
elif Kullanici_Sifre!=SistemKA:
    print("Merhaba {}, Hatali Bir Sifre Girdiniz!!!".format(SistemKA))
