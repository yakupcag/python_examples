import datetime
import time

#plaka:giris_saati
araclar={}
saniyelik_ucret=10
toplam_gelir=0

def arac_giris(plaka):
    if len(plaka)>3:
        araclar[plaka]=datetime.datetime.now()
        print("Araç girişi yapılıyor lütfen bekleyin...")
        time.sleep(3)
        return f"{plaka} girişi yapılmıştır"
    else:
        return "Lütfen geçerli bir plaka girin"

def arac_cikis(plaka):
    global saniyelik_ucret
    global toplam_gelir
    if plaka in araclar:
        ucret=int(((datetime.datetime.now()-araclar[plaka]).total_seconds())*saniyelik_ucret)
        toplam_gelir+=ucret
        del araclar[plaka]
        return (f"Toplam ücret = {ucret} TL")

    else:
        return "Bu plaka otoparkta yok"

def parktaki_araclar():
    if len(araclar)>0:
        for plaka,giris in araclar.items():
            print(f"Plaka = {plaka} --> Giriş saati = {giris}")
    else:
        print("Otopark boş")

print("---BinPark'a Hoşgeldiniz---")

while True:
    print("1) Araç Giriş")
    print("2) Araç Çıkış")
    print("3) Otoparktaki Araçlar")
    print("4) Toplam Gelir")
    print("5) Çıkış")

    try:
        secim=int(input("Lütfen yapmak istediğiniz işlemi girin : "))

        if secim==1:
            try:
                plaka=input("Lütfen plakayı girin : ").upper()
                donut=arac_giris(plaka)
                print(donut)
            except:
                print("Hata oldu tekrar deneyin")
        
        elif secim==2:
            try:
                plaka=input("Lütfen plakayı girin : ").upper()
                donut=arac_cikis(plaka)
                print(donut)
            except:
                print("Hata oldu tekrar deneyin")
        
        elif secim==3:
            parktaki_araclar()

        elif secim==4:
            print(f"Toplam gelir = {toplam_gelir}")

        elif secim==5:
            print("Çıkış yapılıyor lütfen bekleyin...")
            time.sleep(4)
            break

        else:
            print("Hatalı seçim")
    
    except ValueError:
        print("Yanlış seçim")