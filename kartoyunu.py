import random

print("\n---BİNGAMES'e Hoşgeldiniz---\n")

bakiye=1000

while bakiye>0:
    print(f"Bakiyeniz : {bakiye} TL")
    oyuncutoplam=0
    bahis_miktar=int(input("Bahis miktarı girin : "))

    if bahis_miktar<=bakiye:
        bilgisayarkaybetti=False
        oyuncukaybetti=False
        sayicek="E"

        while sayicek=="E":
            sayi=random.randint(1,11)
            print(f"Çekilen sayı {sayi}")
            oyuncutoplam+=sayi
            print(f"Toplam puanınız : {oyuncutoplam}")

            if(oyuncutoplam>21):
                print("Toplam çekilen tutar 21'i geçtiği için bahsi kaybettiniz")
                bakiye-=bahis_miktar
                oyuncukaybetti=True
                break
            
            sayicek=input("Sayı çekmek istiyor musunuz (E/H) : ")
            sayicek=sayicek.upper()
            
        if oyuncukaybetti==False:
            bilgisayar=True
            bilgisayartoplam=0

            while bilgisayar:
                bilgisayarsayicek=random.randint(1,11)
                bilgisayartoplam+=bilgisayarsayicek

                print(f"Bilgisayarın çektiği sayı : {bilgisayarsayicek}")
                print(f"Bilgisayarın çektiği sayılar toplamı : {bilgisayartoplam}")

                if bilgisayartoplam>21:
                    print("Bilgisayarın toplam çekilen tutar 21'i geçtiği için bahsi kazandınız")
                    bakiye+=bahis_miktar
                    bilgisayarkaybetti=True
                    break
                elif bilgisayartoplam>=17:
                    bilgisayar=False

            if bilgisayarkaybetti==False:
                print("-----Toplam Sonuçları-----")
                print(f"Sizin puanınız : {oyuncutoplam}")
                print(f"Bilgisayarın puanı : {bilgisayartoplam}")

                if oyuncutoplam>bilgisayartoplam:
                    print("Tebrikler Kazandınız")
                    bakiye+=bahis_miktar
        
                elif oyuncutoplam<bilgisayartoplam:
                    print("Maalesef Kaybettiniz")
                    bakiye-=bahis_miktar

                else:
                    print("Bilgisayarla aynı puandasınız bakiye iade edildi")

    else:
        print("Oynayacağınız bahis tutarı bakiyenizden büyük olamaz!!!")

if bakiye==0:
    print("Paranız bitti! Oyun bitti. Geçmiş olsun :)")