import random

kelimeler = ["python", "yazilim", "bilgisayar", "donanim"]
secilen_kelime=random.choice(kelimeler)
gorunur_kelime=[]

for i in range(len(secilen_kelime)):
    gorunur_kelime.append("_")

can=5

while can>0:
    harfbulundu=False
    harfal=input("Harf girin : ").lower()


    for i in range(len(secilen_kelime)):
        if harfal==secilen_kelime[i]:
            gorunur_kelime[i]=harfal
            harfbulundu=True

    if harfbulundu==False:
        can-=1
        print(f"Maalesef tahmin ettiğiniz harf kelime de yok canınınz 1 azaldı")
    
    print(f"Canınız : {can}")
    print(*gorunur_kelime)

    if "_" not in gorunur_kelime:
        print(f"Tebrikler kelimeyi buldunuz\nKelime : {secilen_kelime}")
        break
          
else:
    print("Maalesef canınız bitti Kaybettiniz")
    print(f"Seçilen kelime {secilen_kelime}")
