import random
import time

para=100
enerji=100
cpu_gucu=10

hedefler = [
    {"ad": "Mahalle Bakkalı", "zorluk": 20, "odul": 100},
    {"ad": "Şehir Kütüphanesi", "zorluk": 45, "odul": 300},
    {"ad": "Banka Sunucusu", "zorluk": 75, "odul": 1000},
    {"ad": "Pentagon", "zorluk": 95, "odul": 5000}
]

market_urunleri = [
    {"cpu_adet":1,"fiyat":100},
    {"cpu_adet":10,"fiyat":1000},
    {"cpu_adet":20,"fiyat":2000},
    {"cpu_adet":50,"fiyat":5000}
    ]

def saldir(hedef):
    global enerji
    global para
    global cpu_gucu
    hedef-=1
    seclen_hedef=hedefler[hedef]

    if enerji<20:
        return "Maalesef yeterli gücünüz yok. Dinlenmeyi deneyin"
    anlik_cpu_gucu=cpu_gucu+random.randint(1,50)
    enerji-=20

    print("Savaş başladı lütfen sonuçlanmasını bekleyin...")
    time.sleep(5)

    if seclen_hedef["zorluk"]>anlik_cpu_gucu:
        return "Maalesef siber savaşı kaybettiniz"
    para+=seclen_hedef["odul"]

    return f"Tebrikler {seclen_hedef['ad']}' ı hacklediniz. Para hesabınıza eklendi"

def dinlen():
    global enerji
    print("Kullanıcı uyuyor...")
    time.sleep(5)
    enerji=100
    return f"Enerji Fullendi."

def market(urunal):
    global para
    global cpu_gucu
    urunal-=1
    secilenmarket=market_urunleri[urunal]

    if para<secilenmarket["fiyat"]:
        return "Maalesef yeterli bakiyeniz bulunmamaktadır"
    
    cpu_gucu+=secilenmarket["cpu_adet"]
    para-=secilenmarket["fiyat"]

    return f"İşlem Başarılı. Yeni CPU gücünüz : {cpu_gucu}"

def durum_raporu():
    global enerji
    global para
    global cpu_gucu
    return f"Enerjiniz : {enerji}\nBakiyeniz : {para}\nCPU Gücünüz : {cpu_gucu}"



while True:
    print("1) Saldır")
    print("2) Dinlen")
    print("3) Market")
    print("4) Rapor")
    print("5) Çıkış")

    try:
        secim=int(input("Lütfen yapmak istediğiniz işlemi girin : "))

        if secim==1:
            print("0) Geri dön")
            i=1
            for hedef_sozluk in hedefler:
                print(f"{i}) {hedef_sozluk['zorluk']} , {hedef_sozluk['ad']} , {hedef_sozluk['odul']} TL")
                i+=1
            try:
                hedef=int(input("Lütfen saldrılacak hedefi girin : "))
                if hedef>=0 and hedef<i:
                    if hedef==0:
                        continue
                    else:
                        donut=saldir(hedef)
                        print(donut)
                else:
                    print("Hatalı seçim")
            except ValueError:
                print("Hatalı seçim")
            
        elif secim==2:
            donut=dinlen()

            print(donut)

        elif secim==3:
            print("0) Geri dön")
            i=1
            for urunler in market_urunleri:
                print(f"{i}) {urunler['cpu_adet']} CPU gücü : {urunler['fiyat']} TL")
                i+=1
            try:
                urunal=int(input("Lütfen yapmak isteğiniz işlemi seçin girin : "))
                if urunal>=0 and urunal<i:
                    if urunal==0:
                        continue
                    else:
                        donut=market(urunal)
                        print(donut)
                else:
                    print("Hatalı seçim")
            except ValueError:
                print("Hatalı seçim")

        elif secim==4:
            donut=durum_raporu()

            print(donut)

    except ValueError:
         print("Hatalı seçim")