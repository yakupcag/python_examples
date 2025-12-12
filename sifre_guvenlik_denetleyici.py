
print("---Güvenli Şifre Oluşturucu Bota Hoşgeldiniz---")

while True:
    sifreAl=input("Lütfen şifre belirleyin : ")

    buyuk_harf=False
    kucuk_harf=False
    rakam_ara=False
    ozel_karakter=False

    if len(sifreAl)>7:
        for harf in sifreAl:

            if harf.isupper():
                buyuk_harf=True

            if harf.islower():
                kucuk_harf=True

            if harf.isdigit():
                rakam_ara=True

            if harf.isalpha()==False and harf.isdigit()==False:
                ozel_karakter=True
        if buyuk_harf and kucuk_harf and rakam_ara and ozel_karakter:
            print("Tebrikler şifreniz güçlü")
            break
        else:
            if buyuk_harf==False:
                print("Lütfen en az bir büyük harf girin")

            if kucuk_harf==False:
                print("Lütfen en az bir küçük harf girin")

            if rakam_ara==False:
                print("Lütfen en az bir rakam girin")

            if ozel_karakter==False:
                print("Lütfen en az bir özel karakter( #, %, $, vb) girin")
            
    
    else:
        print("Şifre uzunluğu en az 8 olmalı")
