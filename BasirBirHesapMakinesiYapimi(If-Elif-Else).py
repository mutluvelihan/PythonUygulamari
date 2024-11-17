print("""Hesap Makinesine Hosgeldiniz!!!

[1] = TOPLAMA
[2] = CIKARMA
[3] = CARPMA
[4] = BOLME
[5] = US ALMA
[Q] = ÇIKIŞ
""")

islem=input("Lutfen Yapmak İstediginiz İslemi Seciniz: ")

if islem=="1":
    sayi1=float(input("Lutfen Ilk Sayiyi Giriniz: "))
    sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz: "))
    print("Toplama Isleminizin Sonucu {}".format(round(sayi1+sayi2),2))
elif islem=="2":
     sayi1=float(input("Lutfen Ilk Sayiyi Giriniz: "))
     sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz: "))
     print("Çikarma Isleminizin Sonucu {}".format(round(sayi1-sayi2),2))
elif islem=="3":
     sayi1=float(input("Lutfen Ilk Sayiyi Giriniz: "))
     sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz: "))
     print("Çarpma Isleminizin Sonucu {}".format(round(sayi1*sayi2),2))
elif islem=="4":
     sayi1=float(input("Lutfen Ilk Sayiyi Giriniz: "))
     sayi2=float(input("Lutfen Ikinci Sayiyi Giriniz: "))
     print("Bolme Isleminizin Sonucu {}".format(round((sayi1/sayi2),2)))
elif islem=="5":
     sayi1=float(input("Lutfen Ilk Sayiyi Giriniz: "))
     sayi2=float(input("Lutfen Kuvvet Derecesini Giriniz: "))
     print("Us Alma Isleminizin Sonucu {}".format(round(sayi1**sayi2),2))
elif islem=="Q" or islem=="q":
     print("Hoscakalin...")
else:
     print("Gecersiz Islem Yapildi")