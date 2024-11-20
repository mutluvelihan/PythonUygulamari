MorsAlphabet={'A':'.-',
              'B':'-...',
              'C':'-.-.',
              'D':'-..',
              'E':'.',
              'F':'..-.',
              'G':'--.',
              'H':'....',
              'I':'..',
              'J':'.---',
              'K':'-.-',
              'L':'.-..',
              'M':'--',
              'N':'-.',
              'O':'---',
              'P':'.--.',
              'Q':'--.-',
              'R':'.-.',
              'S':'...',
              'T':'-',
              'U':'..-',
              'V':'...-',
              'W':'.--',
              'X':'-..-',
              'Y':'-.--',
              'Z':'--..',
              ' ':'/',        
}

Cumle=input("Lutfen cevirmek istediginiz cumleyi giriniz: ").upper()

for i in range(0,len(Cumle)):
    index=Cumle[i]
    sonuc=MorsAlphabet.get(index)
    print(sonuc, end=" ")