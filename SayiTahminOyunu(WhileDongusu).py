Sayi=25
Hak=10

while Hak>-50:
    Tahmin=int(input("Lutfen Pozitif Bir Tamsayi Giriniz: "))
    if Tahmin<0:
        print("Girdiginiz Sayi Pozitif Bir Tam Sayi Degildir!!!")
        continue
    Hak-=1
    if Sayi==Tahmin:
        print("Dogru Tahmin Ettiniz, Tebrikler :D")
        break
    elif Sayi>Tahmin:
        print("Yukari, Kalan Hakkiniz {}".format(Hak))
    else:
        print("Asagi, Kalan Hakkiniz {}".format(Hak))
    if  Hak==0:
        print("Hakkiniz Kalmamistir. Dogru Sayi {} olacaktir.".format(Sayi))