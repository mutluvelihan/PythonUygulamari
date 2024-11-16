print("Merhaba, Vucut Kitle Endeksi Hesaplama Uygulamasina Hosgeldiniz!")

Boy=int(input("Lutfen Boyunuzu Cm Cinsinden Giriniz:"))
Kilo=int(input("Lutfen Kilonuzu Giriniz:"))

Endeks=round(((Kilo)/(Boy/100)**2),2)

if Endeks<=18.5:
    print("Vucut Kitle Endeksiniz {}'dir. Dusuk Kilolu Grubundasiniz!".format(Endeks))
elif Endeks>18.5 and Endeks<=24.9:
    print("Vucut Kitle Endeksiniz {}'dir. Normal Kilolu Grubundasiniz".format(Endeks))
elif Endeks>25 and Endeks<=29.9:
    print("Vucut Kitle Endeksiniz {}'dir. Fazla Kilolu Grubundasiniz".format(Endeks))
elif Endeks>30 and Endeks<=40:
    print("Vucut Kitle Endeksiniz {}'dir. Obez Grubundasiniz".format(Endeks))
elif Endeks>40:
    print("Vucut Kitle Endeksiniz {}'dir. Asiri Obez Grubundasiniz".format(Endeks))