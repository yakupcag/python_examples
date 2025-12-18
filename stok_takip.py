
stoklar = {"elma": 100, "muz": 50, "ekmek": 20}

def urun_ekle(ad,adet):
    global stoklar
    urunbulundu=False

    for urun_ad,urun_adet in stoklar.items():
        if urun_ad==ad:
            stoklar[ad]=urun_adet+adet
            urunbulundu=True

            return f"{urun_ad} ürünün stoğuna +{adet} eklenmiştir"

    if urunbulundu==False:
        stoklar[ad]=adet
        return f"{ad} ürünü {adet} stokla veri tabanına başarıyla eklenmiştir "

def urun_sat(ad,adet):
    global stoklar
    urunbulundu=False

    for urun_ad,urun_adet in stoklar.items():
        if urun_ad==ad:
            if urun_adet>=adet:
                stoklar[urun_ad]=urun_adet-adet
                urunbulundu=True
                return f"{urun_ad} ürünü {adet} satılmıştır"
            else:
                return "Stok seviyesi yeterli değildir"
            
    if urunbulundu==False:
            return f"{ad} ürünü veri tabanında bulunamamıştır"

def stoklari_goster():
    global stoklar
    return stoklar

print("---BinLojistik'e Hoşgeldiniz---")

while True:
    print("1) Ürün Ekle")
    print("2) Ürün Sat")
    print("3) Stok Sorgula")
    print("4) Çıkış")

    try:
        secim=int(input("Yapmak istediğiniz işlemi girin : "))

        if secim==1:
            try:
                ad=input("Lütfen ürün adını girin : ").lower()
                adet=int(input("Lütfen ürün adedini girin : "))
                donut=urun_ekle(ad,adet)
                print(donut)

            except ValueError:
                print("Yanlış seçim")

        elif secim==2:
            try:
                ad=input("Lütfen ürün adını girin : ").lower()
                adet=int(input("Lütfen ürün adedini girin : "))
                donut=urun_sat(ad,adet)
                print(donut)
                
            except ValueError:
                print("Yanlış seçim")

        elif secim==3:
            sonuc=stoklari_goster()
            for urun_ad,urun_adet in sonuc.items():
                print(f"Ürün Adı :{urun_ad} ---> Stok : {urun_adet}")

        elif secim==4:
            print("Çıkış yapılıyor...")
            break
            
        else:
            print("Yanlış seçim")
    
    except ValueError:
        print("Yanlış seçim")