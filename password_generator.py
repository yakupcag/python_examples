import random

harfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakamlar = "1234567890"
semboller = "+-/*!&$#?=@"

tumalfabe=harfler+rakamlar+semboller

try:
    sifre_uzunluk=int(input("Şifrenizin uzunluğu ne kadar olsun = "))
    sifre=""

    i=0
    while i<sifre_uzunluk:
        

        uretec=random.choice(tumalfabe)
        sifre+=uretec

        i+=1

    print(f"Şifreniz = {sifre}")

except:
    print("Lütfen sayı girin!!!")

