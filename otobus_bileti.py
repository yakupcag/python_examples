koltuklar=['1','2','3','4','5','6','7','8','9','10']

print("\n---Has Bingöl Turizm'e Hoşgeldiniz---\n")

ciro=0
koltukfiyat=500

while True:
    print("1) Koltukları Göster")
    print("2) Bilet Al")
    print("3) Bilet İptal")
    print("4) Toplam Ciro")
    print("0) Çıkış")

    secim=int(input("\nYapmak istediğiniz işlemi seçiniz : "))

    if secim==1:
        print("\nKoltuk durumları : ")
        for koltuk in koltuklar:
            print(f"[{koltuk}]", end=" ")
        print("\n")
    
    elif secim==2:
        secim=int(input("Lütfen almak istediğiniz koltuk numarasını girin : "))
        if koltuklar[secim-1]=="X":
            print("Bu koltuk zaten satılmış !!!")
        else:
            koltuklar[secim-1]="X"
            ciro+=koltukfiyat

    elif secim==3:
        secim=int(input("Lütfen iptal etmek istediğiniz koltuk numarasını girin : "))
        if koltuklar[secim-1]=="X":
            koltuklar[secim-1]=str(secim)
            ciro-=koltukfiyat
        else:
            print("Bu koltuk boş !!!")

    elif secim==4:
        print(f"Toplam Ciro = {ciro} TL")

    elif secim==0:
        break