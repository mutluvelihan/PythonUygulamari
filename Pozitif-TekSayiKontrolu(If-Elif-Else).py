Sayi=int(input("Lutfen Bir Sayi Giriniz: "))
Kontrol=(Sayi>0) and (Sayi%2==1)

if Kontrol==True:
    print("{}, pozitif bir tek sayidir!".format(Sayi))
else:
    print("{}, pozitif bir tek sayi degildir!".format(Sayi))